import sys
import os
from datetime import datetime, date, timedelta
import random

# 添加父目錄到 Python 路徑
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from supabase_client import supabase

# 測試用的心情 emoji 列表
MOOD_EMOJIS = ["😊", "😢", "😡", "😴", "😍", "😎", "🤔", "😭", "😤", "🥰"]

# 測試用的顏色代碼列表
COLOR_CODES = [
    "#FF9999",  # 淺紅色
    "#99FF99",  # 淺綠色
    "#9999FF",  # 淺藍色
    "#FFFF99",  # 淺黃色
    "#FF99FF",  # 淺紫色
    "#99FFFF",  # 淺青色
    "#FFCC99",  # 淺橙色
    "#CC99FF",  # 淺紫羅蘭色
    "#99FFCC",  # 淺薄荷色
    "#FFCCCC"   # 淺粉紅色
]

def generate_test_entries(user_id: int, start_date: date, days: int):
    """生成指定天數的測試日記條目"""
    entries = []
    current_date = start_date
    
    for _ in range(days):
        # 隨機決定是否創建這天的日記（70% 的機率）
        if random.random() < 0.7:
            entry = {
                "user_id": user_id,
                "content_text": f"這是 {current_date} 的日記內容",
                "photo_url": f"https://picsum.photos/200/300?random={random.randint(1, 1000)}",
                "hex_color_code": random.choice(COLOR_CODES),
                "mood_icon_code": random.choice(MOOD_EMOJIS),
                "entry_date": current_date.isoformat(),
                "created_at": datetime.now().isoformat()
            }
            entries.append(entry)
        
        current_date += timedelta(days=1)
    
    return entries

def insert_test_data():
    """插入測試資料到資料庫"""
    try:
        # 生成 2024 年 4 月的測試資料
        start_date = date(2024, 3, 1)
        test_entries = generate_test_entries(
            user_id=8,  # 使用你的用戶 ID
            start_date=start_date,
            days=30  # 4 月有 30 天
        )
        
        # 批量插入資料
        for entry in test_entries:
            result = supabase.table("DIARY_ENTRY").insert(entry).execute()
            print(f"已插入日記條目: {entry['entry_date']}")
        
        print(f"成功插入 {len(test_entries)} 筆測試資料")
        
    except Exception as e:
        print(f"插入測試資料時發生錯誤: {str(e)}")

if __name__ == "__main__":
    insert_test_data() 