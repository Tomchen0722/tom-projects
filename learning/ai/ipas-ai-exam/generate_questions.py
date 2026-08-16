import os
import json
import time
import argparse
from dotenv import load_dotenv
import google.generativeai as genai

# ==========================================
# iPAS AI 應用規劃師 題庫自動生成腳本
# ==========================================

# 讀取 .env 中的設定
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("錯誤：找不到 GEMINI_API_KEY。請在 .env 檔案中設定您的 Gemini API 金鑰。")
    print("格式: GEMINI_API_KEY=your_api_key_here")
    exit(1)

genai.configure(api_key=API_KEY)

# 初始化模型 (使用較強的推理模型)
generation_config = {
  "temperature": 0.7,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-flash-latest",
  generation_config=generation_config,
)

def get_prompt(subject, num_questions, is_scenario=True):
    scenario_prompt = ""
    if is_scenario:
        scenario_prompt = """
        【重要限制】:
        所有的題目都必須是「情境題 (Scenario-based)」。
        每一題都必須包含 `scenario` 欄位，描述一個企業導入、開發、遭遇困難、或者資料分析的具體情境（例如：某銀行正在...、某工廠部署了...、某工程師遇到...）。
        題幹 `stem` 則是針對該情境提出問題。
        """
    else:
        scenario_prompt = """
        【限制】:
        請生成理論、名詞解釋、原則觀念題，不需要有情境。`scenario` 欄位請留空字串 ""。
        """

    subject_names = {
        "s1_beginner": "初級 - 科目一：人工智慧基礎概論",
        "s2_beginner": "初級 - 科目二：生成式 AI 應用與規劃",
        "s1_inter": "中級 - 科目一：AI 技術應用與規劃",
        "s2_inter": "中級 - 科目二：大數據處理分析與應用",
        "s3_inter": "中級 - 科目三：機器學習技術與應用"
    }
    subject_label = subject_names.get(subject, subject)
    
    # 決定大類別 (用於 JSON 的 subject 欄位，如 s1, s2, s3)
    json_subject = subject.split("_")[0]
    level = "beginner" if "beginner" in subject else "intermediate"

    return f"""
    你現在是一位「iPAS AI 應用規劃師」的官方出題委員。
    請為【{subject_label}】生成 {num_questions} 道選擇題。

    {scenario_prompt}

    【難度與風格】:
    - 難度必須符合 {level} 級別。初級偏向觀念與應用，中級偏向技術、除錯、演算法原理及進階規劃。
    - 四個選項 (A, B, C, D) 必須只有一個是正確的。
    - 對於四個選項，都必須給予詳細的解析（為何正確、為何錯誤）。

    【輸出格式】:
    你必須嚴格遵守以下 JSON Array 格式輸出，不要包含任何 Markdown 標記，純 JSON：
    [
      {{
        "level": "{level}",
        "subject": "{json_subject}",
        "subjectLabel": "{subject_label}",
        "scenario": "情境描述 (若無情境題請留空字串)",
        "stem": "題幹描述...",
        "options": ["A選項內容", "B選項內容", "C選項內容", "D選項內容"],
        "answer": 0, // 0~3 代表正確選項的索引
        "explanations": ["A選項的詳細解析", "B選項的詳細解析", "C選項的詳細解析", "D選項的詳細解析"]
      }},
      ...
    ]
    """

def generate_batch(subject, num_questions, is_scenario):
    prompt = get_prompt(subject, num_questions, is_scenario)
    try:
        response = model.generate_content(prompt)
        # response_mime_type 已經強制輸出 JSON，所以 response.text 應該是有效的 JSON 陣列字串
        data = json.loads(response.text)
        return data
    except Exception as e:
        print(f"API 請求或解析失敗: {e}")
        # print("Response content:", response.text if hasattr(response, 'text') else 'No text')
        return None

def main():
    parser = argparse.ArgumentParser(description='生成 iPAS AI 題庫')
    parser.add_argument('--target', type=int, default=100, help='本次要生成的總題數')
    args = parser.parse_args()

    target_questions = args.target
    batch_size = 5 # 每次請求生成 5 題，避免過載與幻覺
    
    # 目標比例：2/3 情境題
    # 我們設定輪詢的科目
    subjects = ["s1_beginner", "s2_beginner", "s1_inter", "s2_inter", "s3_inter"]
    
    # 讀取現有題庫
    file_path = "questions_data.json"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8-sig") as f:
            try:
                db = json.load(f)
            except json.JSONDecodeError:
                db = {"beginner": [], "intermediate": []}
    else:
        db = {"beginner": [], "intermediate": []}

    current_total = len(db["beginner"]) + len(db["intermediate"])
    print(f"目前題庫已有 {current_total} 題，準備開始生成，目標新增 {target_questions} 題...")

    generated_count = 0
    subject_idx = 0
    
    while generated_count < target_questions:
        current_subject = subjects[subject_idx % len(subjects)]
        
        # 依要求全面改為情境題
        is_scenario = True 

        print(f"[{generated_count + 1}/{target_questions}] 正在生成 {batch_size} 題 (科目: {current_subject}, 情境題: {is_scenario})...")
        
        new_questions = generate_batch(current_subject, batch_size, is_scenario)
        
        if new_questions:
            # 進行簡單驗證
            valid_questions = []
            for q in new_questions:
                if all(k in q for k in ["level", "subject", "subjectLabel", "stem", "options", "answer", "explanations"]):
                    if len(q["options"]) == 4 and len(q["explanations"]) == 4:
                        valid_questions.append(q)
            
            for q in valid_questions:
                level = q.pop("level") # 將 level 欄位移出，分別存入 beginner 或 intermediate
                if level == "beginner":
                    db["beginner"].append(q)
                else:
                    db["intermediate"].append(q)
            
            generated_count += len(valid_questions)
            print(f"成功新增 {len(valid_questions)} 題，目前進度：{generated_count}/{target_questions}")
            
            # 儲存到檔案
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(db, f, ensure_ascii=False, indent=2)
                
        else:
            print("生成失敗，暫停 5 秒後重試...")
            time.sleep(5)
            continue
            
        subject_idx += 1
        
        # 避免觸發 API 頻率限制 (Rate Limit)，暫停一下
        time.sleep(3)

    print(f"任務完成！共成功新增 {generated_count} 題。")
    print(f"最新總題數: 初級 {len(db['beginner'])} 題，中級 {len(db['intermediate'])} 題")

if __name__ == "__main__":
    main()
