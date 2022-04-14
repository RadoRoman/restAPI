from fastapi import FastAPI
from models import User, Role
from typing import List

app = FastAPI()

db: List[User] = [User(
    user_name="first_user",
    password="password",
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
    db.append(user)
    return {"username": user.user_name}