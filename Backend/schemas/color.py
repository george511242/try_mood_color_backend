from pydantic import BaseModel
from typing import Optional

class MoodTreeColorResponse(BaseModel):
    hex: str
    owner_name: Optional[str] = None  # owner_name 可以為 null
    content_text: Optional[str] = None  # 新增 content_text 欄位，返回日記內容


class FetchColor(BaseModel):
    hex: str
    owner_name: Optional[str] = None  # owner_name 可以為 null

