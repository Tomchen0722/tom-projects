# -*- coding: utf-8 -*-
"""
TWSE Essay Model Answer Streamliner
Transforms overly verbose model answers (2000+ chars) into concise, punchy benchmarks (700-900 chars)
structured for ~80%+ scoring on 25-point questions under handwritten exam constraints.
"""
import re

def clean_clause(text, max_len=55):
    """Extracts concise, grammatically complete technical clauses without filler text."""
    text = re.sub(r'<.*?>', '', text).strip()
    text = re.sub(r'\s+', ' ', text)
    text = text.lstrip('：:，,、。 ')
    sents = [s.strip() for s in re.split(r'[。\n]', text) if s.strip()]
    if not sents:
        return ""
    first = sents[0]
    if len(first) <= max_len:
        return first.rstrip('：:，,、;； ') + "。"
    clauses = [c.strip() for c in re.split(r'[,，;；]', first) if c.strip()]
    res = ""
    for c in clauses:
        if not res:
            res = c
        elif len(res) + len(c) + 1 <= max_len or len(res) < 24:
            res += "，" + c
        else:
            break
    return res.rstrip('：:，,、;； ') + "。"

def convert_pre_code(m):
    """Converts bulky ASCII diagrams into concise 1-line technical flow representations."""
    code_text = m.group(1).strip()
    lines = [line.strip() for line in code_text.split('\n') if line.strip() and not any(line.strip().startswith(ch) for ch in '┌└├│─═║╔╗╚╝')]
    key_lines = [l for l in lines if any(k in l for k in ['第', '道', '階段', '層', 'Phase', 'Step', 'Level', '->', '→'])]
    if key_lines:
        items = []
        for l in key_lines[:4]:
            clean_l = l.strip('【】[]-* \t\r\n0123456789.:')
            if clean_l:
                items.append(clean_l)
        if items:
            short_flow = " → ".join(items)
            return f"<p><strong>核心架構流程</strong>：{short_flow}。</p>"
    elif lines:
        items = [l.strip('【】[]-* \t\r\n0123456789.:') for l in lines[:3] if l.strip('【】[]-* \t\r\n0123456789.:')]
        if items:
            short_flow = " → ".join(items)
            return f"<p><strong>核心處理流程</strong>：{short_flow}。</p>"
    return ""

def streamline_model_answer(html):
    """
    Streamlines an essay HTML model answer into a concise 80%-score answer.
    Preserves:
    - <h4> section headers
    - <strong> scoring keywords and concrete metrics (RTO, RPO, TLS 1.3, AES-256, WORM, etc.)
    - Direct structured bullet points for each sub-question
    """
    if not html:
        return ""
    html_cleaned = re.sub(r'<pre><code.*?>(.*?)</code></pre>', convert_pre_code, html, flags=re.DOTALL)
    
    sections = re.findall(r'(<h4>.*?</h4>)(.*?)(?=(?:<h4>|$))', html_cleaned, re.DOTALL)
    if not sections:
        return html
        
    condensed_sections = []
    
    for h4, content in sections:
        h4_clean = h4.strip()
        body = content.strip()
        is_intro = any(w in h4_clean for w in ['破題', '背景', '前言', '核心戰略', '核心定位'])
        is_conclusion = any(w in h4_clean for w in ['結論', '結語', '總結', 'SRE 最佳實務', '實務結論'])
        
        # 1. Parse tables into clean key-value bullets
        table_bullets = []
        tables = re.findall(r'<table.*?>(.*?)</table>', body, re.DOTALL)
        for t in tables:
            rows = re.findall(r'<tr>(.*?)</tr>', t, re.DOTALL)
            for r in rows:
                cols = re.findall(r'<td.*?>(.*?)</td>', r, re.DOTALL)
                if len(cols) >= 2:
                    col0 = re.sub(r'<.*?>', '', cols[0]).strip()
                    col1 = re.sub(r'<.*?>', '', cols[1]).strip()
                    col1_short = clean_clause(col1, max_len=45)
                    if col0 and col1_short:
                        table_bullets.append(f"<li><strong>{col0}</strong>：{col1_short}</li>")

        # 2. Parse list items (li)
        lis = re.findall(r'<li.*?>(.*?)</li>', body, re.DOTALL)
        clean_lis = []
        for li in lis:
            li_flat = re.sub(r'<(ul|ol).*?>.*?</\1>', '', li, flags=re.DOTALL).strip()
            if not li_flat:
                continue
            
            m_strong = re.search(r'<strong>(.*?)</strong>\s*[:：]?(.*)', li_flat, re.DOTALL)
            if m_strong:
                title = m_strong.group(1).strip()
                desc = m_strong.group(2).strip()
                desc_clean = clean_clause(desc, max_len=48)
                if desc_clean:
                    clean_lis.append(f"<li><strong>{title}</strong>：{desc_clean}</li>")
                else:
                    clean_lis.append(f"<li><strong>{title}</strong>。</li>")
            else:
                s_clean = clean_clause(li_flat, max_len=48)
                if s_clean:
                    clean_lis.append(f"<li>{s_clean}</li>")

        # 3. Parse paragraphs (p)
        paras = re.findall(r'<p.*?>(.*?)</p>', body, re.DOTALL)
        clean_paras = []
        for p in paras:
            p_clean = clean_clause(p, max_len=60)
            if p_clean:
                clean_paras.append(f"<p>{p_clean}</p>")
                if is_intro or is_conclusion:
                    break

        sec_str = h4_clean + "\n"
        if is_conclusion:
            if clean_paras:
                sec_str += clean_paras[0]
            elif clean_lis:
                sec_str += f"<p>{re.sub(r'<.*?>', '', clean_lis[0])}</p>"
        elif is_intro:
            if clean_paras:
                sec_str += clean_paras[0] + "\n"
            all_bullets = table_bullets + clean_lis
            if all_bullets:
                limit = 6 if len(all_bullets) in [5, 6] else 3
                sec_str += "<ol>\n  " + "\n  ".join(all_bullets[:limit]) + "\n</ol>"
        else:
            all_bullets = table_bullets + clean_lis
            if all_bullets:
                limit = 6 if len(all_bullets) in [5, 6] else 3
                sec_str += "<ol>\n  " + "\n  ".join(all_bullets[:limit]) + "\n</ol>"
            elif clean_paras:
                sec_str += "\n".join(clean_paras[:2])
                
        condensed_sections.append(sec_str.strip())
        
    return "\n\n".join(condensed_sections)
