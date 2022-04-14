from pydantic import BaseModel
from enum import Enum
from typing import List


class Role(str, Enum):
    admin = "admin"
    secretary = "secretary"
    manager = "manager"


class User(BaseModel):
    user_name: str
    password: str
    role: Role