from pydantic import BaseModel
from enum import Enum



class Role(str, Enum):
    admin = "admin"
    secretary = "secretary"
    manager = "manager"


class User(BaseModel):
    user_name: str
    password: str
    role: Role