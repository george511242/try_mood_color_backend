import logging
from datetime import datetime, date
from fastapi import HTTPException, UploadFile, File
from supabase_client import supabase
from controllers.color_controller import generate_color_from_text
from schemas.diary import DiaryEntryCreate, DiaryEntry



logger = logging.getLogger(__name__)


def check_user_exists(user_id: int) -> bool:
    """
    檢查用戶是否存在
    """
    try:
        resp = supabase.table("USER") \
                        .select("id") \
                        .eq("id", user_id) \
                        .single() \
                        .execute()
        return bool(resp.data)
    except Exception:
        logger.exception("檢查用戶存在性時發生錯誤")
        raise HTTPException(500, "Error checking user existence")


def add_diary_entry(entry: DiaryEntryCreate, photo_url) -> DiaryEntry:
    """
    創建一條新的日記條目並返回 Pydantic model
    """
    # 確認用戶存在
    if not check_user_exists(entry.user_id):
        raise HTTPException(404, f"User {entry.user_id} not found")

    # 生成顏色代碼
    hex_color, gemini_comment = generate_color_from_text(entry.content_text)

    # 準備要插入的記錄
    record = {
        "user_id":         entry.user_id,
        "entry_date":      entry.entry_date.isoformat(),
        "content_text":    entry.content_text,
        "mood_icon_code":  entry.mood_icon_code,
        "hex_color_code":  hex_color,
        "created_at":      datetime.utcnow().isoformat(),
        "photo_url":       photo_url
    }

    # 插入到 Supabase
    resp = supabase.table("DIARY_ENTRY").insert(record).execute()
    if not resp.data:
        error = getattr(resp, "error", "Unknown error")
        logger.error(f"日記插入失敗: {error}")
        raise HTTPException(500, f"Failed to create diary entry: {error}")

    # 回傳 Pydantic model
    return DiaryEntry(**resp.data[0]), gemini_comment

def get_diary_entry_by_date(user_id: int, entry_date: str) -> DiaryEntry:
    """
    根據用戶 ID 和日期獲取日記條目
    """
    try:
        resp = supabase.table("DIARY_ENTRY") \
                        .select("*") \
                        .eq("user_id", user_id) \
                        .eq("entry_date", entry_date) \
                        .single() \
                        .execute()
        if not resp.data:
            raise HTTPException(404, "Diary entry not found")
        return DiaryEntry(**resp.data)
    except Exception:
        logger.exception("獲取日記條目時發生錯誤")
        raise HTTPException(500, "Error fetching diary entry")

def delete_by_date(journal_date: date):
    # 執行刪除操作
    response = supabase.table("DIARY_ENTRY").delete().eq("entry_date", journal_date).execute()

    # 檢查是否有資料被刪除
    if not response.data or len(response.data) == 0:
        return {
            "status": "error",
            "message": f"刪除失敗或找不到符合 {journal_date} 的日記資料。"
        }

    # 成功
    return {
        "status": "success",
        "entry_date": journal_date
    }
