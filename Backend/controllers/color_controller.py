import google.generativeai as genai
from fastapi import HTTPException
import logging
import os
from dotenv import load_dotenv
import json
import re

# 設置日誌
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # 輸出到終端機
        logging.FileHandler('app.log')  # 同時輸出到文件
    ]
)
logger = logging.getLogger(__name__)

# 載入環境變數
load_dotenv()

# 配置 Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

genai.configure(api_key=GOOGLE_API_KEY)

def generate_color_from_text(text: str) -> str:
    """
    使用 Gemini API 根據文本內容生成對應的顏色代碼及回覆
    
    Args:
        text (str): 日記內容
        
    Returns:
        tuple: (十六進制顏色代碼, 回覆字串)
    """
    try:
        prompt = f"""
        你是一個「情緒色彩生成與貼心回覆助手」。你的任務是：

        1. 從使用者的日記中分析當下心情。
        2. 產生一組代表該心情的十六進位色碼（HEX code），格式為「#RRGGBB」。
        3. 針對日記內容，給予溫暖、有同理心且具洞察力的回覆。此外，先在開頭說明為何使用此顏色作為日記代表。

        請嚴格按照下面格式輸出（純 JSON，不要多餘文字）：
        ```
        {{
        "hex_code": "#A1B2C3",
        "reply": "這裡放你的回覆……"
        }}
        ```
        日記內容：{text}
        """
        
        logger.info(f"開始生成顏色代碼，輸入文本: {text}")
        
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(prompt)

        # 從正確路徑取出回覆文字
        raw = response.candidates[0].content.parts[0].text
        logger.info(f"API 原始響應文字: {raw}")

        # 用正則擷取大括號內的 JSON 物件
        m = re.search(r"```json\s*(\{.*?\})\s*```", raw, re.S)
        if m:
            json_str = m.group(1)
        else:
            # 如果沒有 fence，就直接當作純 JSON 處理
            json_str = raw

        data = json.loads(json_str)
        logger.info('json格式解析成功')
        logger.info(f"解析後的資料: {data}")

        color_code = data.get("hex_code")
        gemini_comment = data.get("reply")

        if not color_code or not gemini_comment:
            logger.error("API 響應中缺少 hex_code 或 reply")
            raise HTTPException(
                status_code=500,
                detail="API response missing hex_code or reply"
            )
        
        if not color_code.startswith("#") or len(color_code) != 7:
            logger.error(f"無效的顏色代碼格式: {color_code}")
            raise HTTPException(
                status_code=500,
                detail=f"Invalid color code format: {color_code}"
            )
        
        logger.info(f"成功生成顏色代碼: {color_code}")
        logger.info(f"Gemini 回覆: {gemini_comment}")
        return color_code, gemini_comment

    except Exception as e:
        logger.error(f"生成顏色代碼時發生錯誤: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error generating color code: {str(e)}"
        )
