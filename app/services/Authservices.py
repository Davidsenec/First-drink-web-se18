import bcrypt
from datetime import datetime, timedelta, timezone
import jwt
from fastapi import HTTPException, status
from dotenv import load_dotenv
import os
from app.models.user import User
<<<<<<< HEAD
from sqlalchemy.orm import Session
from app.dtos.user import UserRegister, UserLogin, UserResponse
=======
from app.dtos.user import UserRegister,UserLogin,UserResponse
from app.repositories.user_repositories import UserRepository
>>>>>>> 19f922f (add router for login and register)

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


class AuthServices:
    @staticmethod
    def create_access_token(
        data: dict, expires_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES
    ) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def hash_password(plain_password: str) -> str:
        salt = bcrypt.gensalt()
        bytes = plain_password.encode("utf-8")
        hashed = bcrypt.hashpw(bytes, salt)
        return hashed.decode("utf-8")

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        user_byte = plain_password.encode("utf-8")
        hash_byte = hashed_password.encode("utf-8")
        result = bcrypt.checkpw(user_byte, hash_byte)
        return result

    @staticmethod
<<<<<<< HEAD
    def register(db: Session, user_in: UserRegister):
        user_check = db.query(User).filter(User.user_name == user_in.user_name).first()
=======
    def register(repo: UserRepository,user_in:UserRegister):
        user_check = repo.check_user(user_in.user_name)
>>>>>>> 19f922f (add router for login and register)

        if user_check:
            raise HTTPException(status_code=400, detail="Username already used.")

        hashed_password = AuthServices.hash_password(user_in.password)
<<<<<<< HEAD
        new_user = User(
            **user_in.model_dump(exclude={"password"}), hashed_password=hashed_password
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
=======
        new_user= User(**user_in.model_dump(exclude={"password"}),
                       hashed_password =  hashed_password
                       )
        repo.add_user(new_user)
>>>>>>> 19f922f (add router for login and register)
        user_return = UserResponse(
            full_name=user_in.full_name,
            nick_name=user_in.nick_name,
            contact_info=user_in.contact_info,
            address=user_in.address,
        )
        return user_return

    @staticmethod
<<<<<<< HEAD
    def login(db: Session, user_in: UserLogin):
        user_check = db.query(User).filter(User.user_name == user_in.user_name).first()
        if not user_check or not AuthServices.verify_password(
            user_in.password, user_check.hashed_password
        ):
            raise HTTPException(
                status_code=401,
                detail="incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        elif not AuthServices.verify_password(
            user_in.password, user_check.hashed_password
        ):
            raise HTTPException(
                status_code=401,
                detail="incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        token_payload = {"sub": user_check.user_name}
=======
    def login(repo: UserRepository,user_in:UserLogin):
        user_check = repo.check_user(user_in.user_name)
        if not user_check or not AuthServices.verify_password(user_in.password,user_check.hashed_password):
            raise HTTPException(status_code=401,detail="incorrect username or password",headers={"WWW-Authenticate": "Bearer"},)
        elif not AuthServices.verify_password(user_in.password,user_check.hashed_password):
            raise HTTPException(status_code=401,detail="incorrect username or password",headers={"WWW-Authenticate": "Bearer"},)
        token_payload = {"sub":user_check.user_name}
>>>>>>> 19f922f (add router for login and register)
        token = AuthServices.create_access_token(token_payload)
        return {"access_token": token, "token_type": "bearer"}

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
