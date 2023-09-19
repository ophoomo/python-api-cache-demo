# import library ที่ต้องใช้งาน
from functools import lru_cache
from fastapi import FastAPI
from app.models.member_model import Member
from app.routers import member_router
from app.configs.database import engine

# เรียกใช้งาน library fastapi
app = FastAPI()

# กำหนด path ให้ เมื่อส่งค่าไปแบบ POST มาที่ http://[myhost]:[myport]/ จะไปทำงาน function health_check
@app.get("/")
async def health_check():
    return {"status": True}

# กำหนด router ให้ไปทำที่ member_router และกำหนด pathให้เริ่มต้นก็จะได้แบบนี้ http://[myhost]:[myport]/member
app.include_router(member_router.router, prefix="/member", tags="member")