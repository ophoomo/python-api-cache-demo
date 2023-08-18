# import library ที่ต้องใช้งาน
from sqlalchemy import Boolean, Column, Integer, String
from app.configs.database import Base, engine

# สร้าง class ชื่อ member แล้วส่ง function Base จาก config.database เข้าไป
class Member(Base):
    # ชื่อ table ใน database
    __tablename__ = "members"

    # field หรือ column ต่างๆใน database
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    is_active = Column(Boolean, default=True)

Base.metadata.create_all(engine)