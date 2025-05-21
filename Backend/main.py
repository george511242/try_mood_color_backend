# Backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user import router as user_router
from routes.diary import router as diary_router
from routes.mood_tree import router as mood_tree_router
from routes.share import router as share_router  # 引入新的 share 路由
from routes.emoji import router as emoji_router

app = FastAPI()

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允許所有來源
    allow_credentials=True,
    allow_methods=["*"],  # 允許所有方法
    allow_headers=["*"],  # 允許所有標頭
)

# Include routers
app.include_router(user_router, prefix="/api")
app.include_router(diary_router, prefix="/api")
app.include_router(mood_tree_router, prefix="/api")
app.include_router(share_router, prefix="/api")  # 將新的 share 路由加入
app.include_router(emoji_router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "Welcome to MoodColor API"}
