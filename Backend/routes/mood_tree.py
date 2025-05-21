from fastapi import APIRouter, HTTPException
from datetime import datetime
from schemas.color import MoodTreeColorResponse
from controllers.mood_tree_controller import get_mood_color_by_date_and_user

router = APIRouter()

@router.get("/mood_tree_color/{user_id}/{date}", response_model=MoodTreeColorResponse)
async def get_mood_tree_color(user_id: int, date: str):
    # 解析傳入的日期 (date 是一個字串，將其轉換為 date 對象)
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Please use YYYY-MM-DD.")

    # 從控制器中獲取指定日期的情緒顏色資料
    result = get_mood_color_by_date_and_user(date_obj, user_id)
    
    # 返回顏色、用戶名稱和內容
    return result
