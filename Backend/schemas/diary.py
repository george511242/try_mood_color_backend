from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class DiaryEntryCreate(BaseModel):
    """
    創建日記條目的請求模型
    """
    user_id: int
    entry_date: date
    content_text: str  # 前端使用 content
    mood_icon_code: Optional[str] = None

class DiaryEntry(DiaryEntryCreate):
    """
    日記條目的完整模型，包含所有欄位
    """
    id: int
    hex_color_code: str
    created_at: datetime
    photo_url: Optional[str] = None

class DiaryEntryResponse(BaseModel):
    """
    日記條目的響應模型
    """
    status: str
    diary_entry: DiaryEntry
    gemini_comment: str

class DeleteDiaryResponse(BaseModel):
    status: str
    entry_date: date
