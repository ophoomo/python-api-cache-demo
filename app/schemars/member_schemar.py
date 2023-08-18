from typing import Union

from pydantic import BaseModel

class MemberBase(BaseModel):
    email: str
    firstname: str
    lastname: str

class Member(MemberBase):
    id: int
    is_active: bool