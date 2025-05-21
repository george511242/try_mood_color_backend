from supabase_client import supabase
from datetime import date
from fastapi import HTTPException

def get_mood_color_by_date_and_user(date: date, user_id: int):
    print(f"Getting mood for: {date} and user_id: {user_id}")
    
    # 查詢 DIARY_ENTRY 表格，並查找指定日期和 user_id 的資料
    response = supabase.table("DIARY_ENTRY")\
        .select("hex_color_code", "user_id", "created_at", "content_text")\
        .eq("entry_date", date)\
        .eq("user_id", user_id)\
        .order("created_at", desc=True)\
        .limit(1).execute()  # 使用 limit(1) 確保最多只返回最新的一條資料
    
    # 檢查是否有找到資料
    if not response.data:
        raise HTTPException(status_code=404, detail="未找到對應日期或用戶的顏色資料")

    # 獲取 user_id 從 DIARY_ENTRY 中查詢的結果
    user_id = response.data[0]["user_id"]

    # 查詢 USER 表格，根據 user_id 查找用戶名稱
    user_response = supabase.table("USER")\
        .select("username")\
        .eq("id", user_id)\
        .limit(1).execute()  # 使用 limit(1) 確保最多只返回 1 行

    # 檢查 user_response 是否有結果
    if not user_response.data:
        raise HTTPException(status_code=404, detail="未找到對應用戶資料")

    # 返回顏色、用戶名稱和內容
    return {
        "hex": response.data[0]["hex_color_code"],  # 正確訪問 response.data[0]
        "owner_name": user_response.data[0]["username"],  # 正確訪問 user_response.data[0]
        "content_text": response.data[0]["content_text"]  # 正確訪問 content_text
    }
