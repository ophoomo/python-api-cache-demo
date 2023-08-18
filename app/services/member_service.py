# import library ที่ต้องใช้งาน
from sqlalchemy.orm import Session
from app.models.member_model import Member
from app.schemars.member_schemar import MemberBase

# find_member คือ function สำหรับดึงข้อมูล member จาก database
async def find_member(db: Session):
    return db.query(Member).all()

# find_member_by_id คือ function สำหรับดึงข้อมูล member โดยอ้างอิงจาก ID จาก database
async def find_member_by_id(db: Session, id: int):
    return db.query(Member).filter(Member.id == id).first()

# create_member คือ function สำหรับเพิ่มข้อมูล member ไปยัง database
async def create_member(db: Session, member: MemberBase):
    _member = Member(email=member.email, firstname=member.firstname, lastname=member.lastname)
    db.add(_member)
    db.commit()
    db.refresh(_member)
    return _member

# remove_member คือ function สำหรับลบข้อมูล member จาก database
async def remove_member(db: Session, id: int):
    _member = find_member_by_id(db=db, id=id)
    db.delete(_member)
    db.commit()