import os
import io
import base64
from datetime import datetime
from dotenv import load_dotenv

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

import google.generativeai as genai

# 設定所需的 Google API 權限範圍
# Gmail: 讀取權限, Drive: 建立與編輯自己上傳的檔案權限
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/drive.file'
]

def authenticate_google():
    """驗證 Google API 並回傳憑證"""
    creds = None
    # token.json 儲存使用者的存取權杖與更新權杖
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # 如果沒有有效憑證，則讓使用者登入
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                print("❌ 找不到 credentials.json！")
                print("請至 Google Cloud Console 下載憑證，並將其改名為 credentials.json 放在這個資料夾。")
                exit(1)
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # 儲存憑證供下次使用
        with open('token.json', 'w', encoding='utf-8') as token:
            token.write(creds.to_json())
            
    return creds

def get_recent_emails(gmail_service):
    """取得過去 24 小時的重要信件"""
    # 搜尋條件：一天內，排除廣告與社群論壇信件
    query = "newer_than:1d -category:promotions -category:social"
    
    results = gmail_service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])
    
    email_data = []
    
    if not messages:
        return email_data
        
    for msg in messages:
        # 取得信件詳細內容
        msg_detail = gmail_service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        
        headers = msg_detail['payload'].get('headers', [])
        subject = next((h['value'] for h in headers if h['name'].lower() == 'subject'), '無主旨')
        sender = next((h['value'] for h in headers if h['name'].lower() == 'from'), '未知寄件者')
        
        # 解析信件內文 (簡化處理純文字部分)
        body = ""
        payload = msg_detail['payload']
        parts = payload.get('parts', [])
        
        # 遞迴尋找 text/plain 的內容
        def extract_text(parts):
            text = ""
            for part in parts:
                if part['mimeType'] == 'text/plain':
                    data = part['body'].get('data', '')
                    if data:
                        text += base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore')
                elif 'parts' in part:
                    text += extract_text(part['parts'])
            return text
            
        if parts:
            body = extract_text(parts)
        else:
            data = payload['body'].get('data', '')
            if data:
                body = base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore')
                
        # 截斷過長的內文避免 AI Token 超標
        body = body[:2000].strip()
        if body:
            email_data.append({
                'subject': subject,
                'sender': sender,
                'body': body
            })
        
    return email_data

def summarize_emails_with_ai(email_data):
    """使用 Gemini AI 將信件內容進行總結"""
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key or api_key == 'your_gemini_api_key_here':
        print("❌ 未設定有效的 GEMINI_API_KEY。請修改 .env 檔案。")
        exit(1)
        
    genai.configure(api_key=api_key)
    
    # 組合信件內容
    content = "以下是我過去 24 小時收到的信件：\n\n"
    for idx, email in enumerate(email_data, 1):
        content += f"【信件 {idx}】\n"
        content += f"寄件者: {email['sender']}\n"
        content += f"主旨: {email['subject']}\n"
        content += f"內容: {email['body']}\n"
        content += "-" * 40 + "\n"
        
    prompt = f"""
    你是一位專業的個人秘書。請根據以下信件內容，幫我整理出一份結構清晰的「每日信件總結報告」。
    報告必須包含以下部分，請使用 Markdown 語法呈現，並讓排版易於閱讀：
    
    1. 💡 重要信件摘要：請列出最重要的 3~5 件事情。
    2. ✅ 待辦事項 (Action Items)：如果有需要我回覆或處理的任務，請明確列出。
    3. 📅 快速瀏覽：用簡短的清單概述次要的信件。
    
    {content}
    """
    
    # 使用 gemini-1.5-flash 模型 (快速且支援大文本)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    
    return response.text

def upload_to_drive(drive_service, summary_text):
    """將摘要存成 Google Doc 上傳到 Google Drive"""
    date_str = datetime.now().strftime("%Y-%m-%d")
    title = f'每日信件摘要 - {date_str}'
    
    file_metadata = {
        'name': title,
        'mimeType': 'application/vnd.google-apps.document'
    }
    
    # 將純文字轉為檔案流以供上傳，這會被自動轉換成 Google Docs 格式
    media = MediaIoBaseUpload(
        io.BytesIO(summary_text.encode('utf-8')), 
        mimetype='text/plain', 
        resumable=True
    )
    
    file = drive_service.files().create(
        body=file_metadata, 
        media_body=media, 
        fields='id'
    ).execute()
    
    print(f"✅ 已成功建立 Google Doc 摘要！檔案名稱: {title}")
    print(f"📂 檔案 ID: {file.get('id')}")

def main():
    print("🔄 開始驗證 Google 權限...")
    creds = authenticate_google()
    
    gmail_service = build('gmail', 'v1', credentials=creds)
    drive_service = build('drive', 'v3', credentials=creds)
    
    print("📥 正在從 Gmail 讀取最新信件 (過濾廣告/社群)...")
    emails = get_recent_emails(gmail_service)
    
    if not emails:
        print("✨ 恭喜！過去 24 小時內沒有新郵件。")
        return
        
    print(f"找到 {len(emails)} 封信件。🤖 正在請 Gemini 進行 AI 摘要...")
    summary = summarize_emails_with_ai(emails)
    
    print("☁️ 正在將結果上傳至 Google Drive...")
    upload_to_drive(drive_service, summary)
    
    print("\n🎉 自動化流程執行完畢！您可以到 NotebookLM 中同步這份新文件了。")

if __name__ == '__main__':
    main()
