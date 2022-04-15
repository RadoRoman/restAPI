import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
import os


class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = os.getenv("APP_SECRET_STRING")
    #secret = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def encode_token(self, role):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=30),
            'iat': datetime.utcnow(),
            'scope': 'token',
            'sub': role
        }
        encoded_jwt = jwt.JWT.encode(payload, self.secret, algorithm= self.ALGORITHM)
        return encoded_jwt

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Signature has expired')
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail='Invalid token')

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)