# import library ที่ต้องใช้งาน
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


# สร้าง class ชื่อ member แล้วส่ง function BaseSettings เข้าไป
class Settings(BaseSettings):
    DB_ENDPOINT: str = "localhost"
    DB_USERNAME: str = "root"
    DB_PASSWORD: str = ""
    DB_PORT: int = 5432
    DB_NAME: str = ""

    REDIS_ENDPOINT: str = "localhost"
    REDIS_USERNAME: str = ""
    REDIS_PASSWORD: str = ""
    REDIS_PORT: int = 6379
    model_config = SettingsConfigDict(env_file=".env")

@lru_cache()
def get_settings():
    return Settings()