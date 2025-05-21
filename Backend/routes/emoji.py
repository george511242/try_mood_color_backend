from fastapi import APIRouter, HTTPException, Path
from controllers.emoji_controller import get_this_month_emoji
from schemas.emoji import ThisMonthEmojiResponse
import logging

# 設置日誌
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(
    tags=["emoji"]
)

@router.get("/this_month_emoji/{user_id}/{year_month}", response_model=ThisMonthEmojiResponse)
async def get_monthly_emoji(
    user_id: int = Path(..., description="用戶 ID"),
    year_month: str = Path(..., description="格式為 YYYY-MM 的月份字符串")
):
    """
    獲取指定用戶在指定月份的每日 emoji 數據
    
    Args:
        user_id (int): 用戶 ID
        year_month (str): 格式為 "YYYY-MM" 的月份字符串
        
    Returns:
        ThisMonthEmojiResponse: 包含該月份所有日期的 emoji 數據
    """
    try:
        logger.info(f"API 請求: 獲取用戶 {user_id} 在 {year_month} 的 emoji 數據")
        return get_this_month_emoji(user_id, year_month)
    except HTTPException as e:
        logger.error(f"API 錯誤: {str(e)}")
        raise e
    except Exception as e:
        logger.error(f"API 內部錯誤: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        ) 