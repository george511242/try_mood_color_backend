from fastapi import APIRouter, UploadFile, HTTPException, File, Form
from controllers.diary_controller import add_diary_entry, get_diary_entry_by_date, delete_by_date
from controllers.google_drive_controller import upload_image_to_drive
from fastapi.responses import JSONResponse
from schemas.diary import DiaryEntryCreate, DiaryEntryResponse, DeleteDiaryResponse
import tempfile
import os
from datetime import date
from starlette.concurrency import run_in_threadpool

router = APIRouter(tags=["diary"])

@router.post("/Post_diary_entry")
async def post_diary_entry(
    user_id: int              = Form(...),
    entry_date: date          = Form(...),
    content_text: str         = Form(...),
    mood_icon_code: str       = Form(...),
    file: UploadFile | None   = File(None)
):
    """
    Create a new diary entry.
    
    Args:
        entry (DiaryEntryCreate): The diary entry data to create
        
    Returns:
        JSONResponse: The created diary entry or an error message
    """

    entry = DiaryEntryCreate(
        user_id        = user_id,
        entry_date     = entry_date,
        content_text   = content_text,
        mood_icon_code = mood_icon_code
    )

    try:
        # ——— 1. 处理图片上传 ———
        photo_url: str | None = None
        if file:
            ext = os.path.splitext(file.filename)[1]
            data = await file.read()  # 一定要 await
            with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
                tmp.write(data)
                tmp_path = tmp.name

            # call sync upload in threadpool to avoid blocking
            photo_url = await run_in_threadpool(upload_image_to_drive, tmp_path)
            os.unlink(tmp_path)

        # Add the entry to the database
        diary_entry, gemini_comment = add_diary_entry(entry, photo_url=photo_url)
        
        return {"status": "success", "diary_entry": diary_entry, "gemini_comment": gemini_comment}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@router.get("/Get_diary_entry/{userid}/{date}")
async def get_diary_entry(user_id: int, entry_date: date):
    """
    Get a diary entry by user ID and entry date.
    
    Args:
        user_id (int): The ID of the user
        entry_date (date): The date of the diary entry (format: YYYY-MM-DD)
        
    Returns:
        JSONResponse: The diary entry or an error message
    """
    try:
        # Call the controller function to get the diary entry
        diary_entry = get_diary_entry_by_date(user_id, entry_date)
        
        return {"status": "success", "diary_entry": diary_entry}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@router.delete("/delete/{journal_date}", response_model=DeleteDiaryResponse)
async def delete_journey(journal_date: date):
    result = delete_by_date(journal_date)
    
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    
    return result


