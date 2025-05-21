from pydantic import BaseModel
from datetime import date
from typing import List

class DailyEmoji(BaseModel):
    date: date
    emoji: str

class ThisMonthEmojiResponse(BaseModel):
    month: str  # 例如 "2024-04"
    emojis: List[DailyEmoji]  # 每天的 emoji 數據 