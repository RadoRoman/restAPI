import time
from fastapi import FastAPI, Request
from models import User, Role
from typing import List
from passlib.hash import pbkdf2_sha256
from passlib.context import CryptContext

app = FastAPI()


db: List[User] = [User(
    user_name="first_user",
    password=pbkdf2_sha256.hash("password"),
    role = Role.admin
)]

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_pwd, hashed_pwd):
    return pwd_context.verify(plain_pwd, hashed_pwd)

def get_password_hash(password):
    return pwd_context.hash(password)


@app.get('/')
def root():
    return {"Hi": "World, Im here"}

@app.get('/api/users')
async def get_users():
    return db


@app.post('/api/create_user')
async def register_user(user: User):
    user.password = pbkdf2_sha256.hash(user.password)
    db.append(user)
    # if user.user_name in db:
    #     pass

    return {"message": f" new user {user.user_name} created"}

# @app.get('/api/{user_name}/{password}')
# async def token_for_user(user_name: User, password: User):
#     dehashed_pw = pbkdf2_sha256.verify(password, User.password)
#     if user_name and dehashed_pw in db:
#         return{"message":"Password found"}
    
#     return{"message":"Password not found"}