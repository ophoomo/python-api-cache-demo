# import library ที่ต้องใช้งาน
import json
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.configs.database import get_db
from app.configs.redis import AlchemyEncoder, get_redis
from app.schemars.member_schemar import MemberBase
from app.models.member_model import Member

from app.services import member_service

# เรียกใช้งาน คำสั่ง APIRouter ของ fastapi ไว้สำหรับกำหนด path
router = APIRouter()

# เรียกใช้งาน redis
r = get_redis()

# กำหนด path ให้ เมื่อเข้ามาที่ http://[myhost]:[myport]/member จะไปทำงาน function get_all_member
@router.get("/")
async def get_all_member(db: Session=Depends(get_db)):
    _members = member_service.find_member(db)
    return { "status": True, "data": _members }

# กำหนด path ให้ เมื่อเข้ามาที่ http://[myhost]:[myport]/member/cache จะไปทำงาน function get_all_member_cache
@router.get("/cache")
async def get_all_member_cache(db: Session=Depends(get_db)):
    # query ข้อมูลจาก redis
    _members = r.get("members")
    # เช็คว่ามีข้อมูล หรือ ไม่
    if _members is not None:
        return { "status": True, "data": json.loads(_members) }

    _members = await member_service.find_member(db)
    # นำข้อมูลทที่ได้จาก database เก็บลง redis เป็นเวลา 5 นาที
    r.set("members", json.dumps(_members, cls=AlchemyEncoder), ex=300)
    return { "status": True, "data": _members }

# กำหนด path ให้ เมื่อส่งค่าไปแบบ POST มาที่ http://[myhost]:[myport]/member จะไปทำงาน function create_member
@router.post("/", status_code=201)
async def create_member(item: MemberBase, db: Session=Depends(get_db)):
    _member = member_service.create_member(db, item)
    return { "status": True, "data": _member }

# กำหนด path ให้ เมื่อส่งค่าไปแบบ DELETE มาที่ http://[myhost]:[myport]/member จะไปทำงาน function delete_member
@router.delete("/{id}", status_code=204)
async def delete_member(id: int, db: Session=Depends(get_db)):
    member_service.remove_member(db, id)
    return { "status": True }