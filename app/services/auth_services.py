import bcrypt
from datetime import datetime, timedelta, timezone
import jwt
from fastapi import HTTPException, status
from dotenv import load_dotenv
import os
from app.models.user import User
from app.dtos.user import UserRegister, UserLogin, UserResponse
from app.repositories.user_repositories import UserRepository

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


class AuthServices:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create_access_token(
        data: dict, expires_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES
    ) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    def hash_password(plain_password: str) -> str:
        salt = bcrypt.gensalt()
        bytes = plain_password.encode("utf-8")
        hashed = bcrypt.hashpw(bytes, salt)
        return hashed.decode("utf-8")

    def verify_password(plain_password: str, hashed_password: str) -> bool:
        user_byte = plain_password.encode("utf-8")
        hash_byte = hashed_password.encode("utf-8")
        result = bcrypt.checkpw(user_byte, hash_byte)
        return result

    def register(self, user_in: UserRegister) -> UserResponse:
        user_check = self.repo.check_user(user_in.user_name)

        if user_check:
            raise HTTPException(status_code=400, detail="Username already used.")

        hashed_password = AuthServices.hash_password(user_in.password)
        new_user = User(
            **user_in.model_dump(exclude={"password"}), hashed_password=hashed_password
        )
        self.repo.add_user(new_user)
        return new_user

    def login(self, user_in: UserLogin):
        user_check = self.repo.check_user(user_in.user_name)
        if not user_check or not AuthServices.verify_password(
            user_in.password, user_check.hashed_password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        token_payload = {"sub": user_check.user_name}
        token = AuthServices.create_access_token(token_payload)
        return {
            "access_token": token,
            "token_type": "bearer",
            "is_admin": user_check.is_admin,
        }

    @staticmethod
    def check_jwt(token: str) -> dict:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired"
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
            )
