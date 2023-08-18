# import library ที่ต้องใช้งาน
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.configs.setting import get_settings

setting = get_settings()

# ประกาศตัวแปรมาเก็บ path สำหรับ connect เข้า database
SQLALCHEMY_DATABASE_URL = "postgresql://{0}:{1}@{2}:{3}/{4}".format(setting.DB_USERNAME, setting.DB_PASSWORD,
 setting.DB_ENDPOINT, setting.DB_PORT, setting.DB_NAME)

# กำหนด config ต่างๆในการเชื่อมไปยัง database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()