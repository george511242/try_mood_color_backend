from supabase_client import supabase
from datetime import datetime, date, timedelta
from typing import List
from schemas.emoji import DailyEmoji, ThisMonthEmojiResponse
import logging
from fastapi import HTTPException

# 設置日誌
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_this_month_emoji(user_id: int, year_month: str) -> ThisMonthEmojiResponse:
    """
    獲取指定用戶在指定月份的每日 emoji 數據
    
    Args:
        user_id (int): 用戶 ID
        year_month (str): 格式為 "YYYY-MM" 的月份字符串
        
    Returns:
        ThisMonthEmojiResponse: 包含該月份所有日期的 emoji 數據
    """
    try:
        logger.info(f"開始獲取用戶 {user_id} 在 {year_month} 的 emoji 數據")
        
        # 驗證用戶是否存在
        user_response = supabase.table("USER").select("id").eq("id", user_id).execute()
        if not user_response.data:
            logger.error(f"用戶 {user_id} 不存在")
            raise HTTPException(status_code=404, detail="User not found")
        
        # 解析年月
        year, month = map(int, year_month.split('-'))
        logger.info(f"解析後的年月: {year}年{month}月")
        
        # 計算該月的第一天和最後一天
        first_day = date(year, month, 1)
        if month == 12:
            last_day = date(year + 1, 1, 1)
        else:
            last_day = date(year, month + 1, 1)
        
        logger.info(f"查詢日期範圍: {first_day} 到 {last_day}")
        
        # 從資料庫獲取該月的日記條目，加入用戶篩選
        response = supabase.table("DIARY_ENTRY") \
            .select("entry_date, mood_icon_code") \
            .eq("user_id", user_id) \
            .gte("entry_date", first_day.isoformat()) \
            .lt("entry_date", last_day.isoformat()) \
            .execute()
        
        logger.info(f"資料庫查詢結果: {response.data}")
        
        # 創建日期到 emoji 的映射
        date_emoji_map = {
            entry["entry_date"]: entry["mood_icon_code"]
            for entry in response.data
        }
        
        logger.info(f"日期到 emoji 的映射: {date_emoji_map}")
        
        # 生成該月所有日期的列表
        current_date = first_day
        daily_emojis = []
        
        while current_date < last_day:
            emoji = date_emoji_map.get(current_date.isoformat(), None)
            if emoji:
                daily_emojis.append(DailyEmoji(
                    date=current_date,
                    emoji=emoji
                ))
            # 使用 timedelta 來安全地增加日期
            current_date += timedelta(days=1)
        
        logger.info(f"生成的每日 emoji 列表: {daily_emojis}")
        
        return ThisMonthEmojiResponse(
            month=year_month,
            emojis=daily_emojis
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"獲取 emoji 數據時發生錯誤: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching monthly emoji data: {str(e)}"
        ) 