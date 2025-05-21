# routes/share.py
from fastapi import APIRouter, HTTPException
from schemas.share import ShareResponse
from controllers.share_controller import share_with_friend, accept_invite, fetch_color
from schemas.color import FetchColor
from schemas.accept_response import AcceptResponse

router = APIRouter()

@router.post("/share/{userid}/{anotheruserid}/{diary_id}", response_model=ShareResponse)
async def share_with_friend_route(userid: int, anotheruserid: int, diary_id: int):
    # 呼叫控制器函數處理分享邏輯
    result = share_with_friend(userid, anotheruserid, diary_id)

    # 若插入失敗，回傳錯誤訊息
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])

    return result

@router.post("/accept/{userid}/{anotheruserid}/{diary_id}", response_model=AcceptResponse)
async def accept_invite_route(userid: int, anotheruserid: int, diary_id: int):
    result = accept_invite(userid, anotheruserid, diary_id)
    return result

@router.get("/fetch_color/{userid}/{anotheruserid}", response_model=FetchColor)
async def fetch_color_route(userid: int, anotheruserid: int):
    result = fetch_color(userid, anotheruserid)
    return result