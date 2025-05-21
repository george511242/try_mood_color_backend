# Backend/routes/user.py
from fastapi import APIRouter
from controllers.user_controller import get_user_by_id, add_user, check_user_exists
from fastapi.responses import JSONResponse
from schemas.user import UserCreate, UserResponse
from typing import Optional
from datetime import datetime

router = APIRouter(tags=["user"])

@router.get("/user/{user_id}")
def read_user(user_id: int):
    return get_user_by_id(user_id)

@router.post("/user", response_model=UserResponse)
async def create_user(user: UserCreate):
    try:
        # Convert Pydantic model to dict and add timestamp
        user_data = user.dict()
        user_data["created_at"] = datetime.now().isoformat()
        
        result = add_user(user_data)
        return JSONResponse(
            status_code=201,
            content={"message": "User created successfully", "user": result}
        )
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"message": str(e)}
        )

# write an api that apply the login and set email as the acocunt
@router.get("/user/login/{email}/{password}")
async def login_user(email: str, password: str):
    response = check_user_exists(email, password)
    if response:
        return JSONResponse(
            status_code=200,
            content={"status": "success", "userid": response}
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"status": "error", "message": "User not found or password incorrect"}
        )

        