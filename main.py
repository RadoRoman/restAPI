from fastapi import FastAPI
from models import User, Role
from typing import List
from passlib.context import CryptContext


app = FastAPI()

pwd_context = CryptContext(schemes = ["bcrypt"], deprecated="auto")

def pwd_hashing(password: str) -> None: 
    return pwd_context.hash(password)

db: List[User] = [User(
    user_name="first_user",
    password=pwd_hashing("password"),
    role = Role.admin
)]


    


@app.get('/')
def root():
    return {"Hi": "World, Im here"}

@app.get('/api/users')
async def get_users():
    return db


@app.post('/api/post_user')
async def register_user(user: User):
    user.password = pwd_hashing(user.password)
    db.append(user)
    return {"message": f" new user {user.user_name} created"}