from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.repositories.user_repositories import UserRepository
from app.services.Authservices import AuthServices
from app.dtos.user import UserRegister, UserLogin, UserResponse
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

router = APIRouter()


def get_user_repo(db: Session = Depends(get_db)):
    return UserRepository(db)


@router.post(
    "/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse
)
def register(user_in: UserRegister, repo: UserRepository = Depends(get_user_repo)):
    return AuthServices.register(repo, user_in)


@router.post("/login")
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    repo: UserRepository = Depends(get_user_repo),
):
    user_in = UserLogin(user_name=form_data.username, password=form_data.password)
    return AuthServices.login(repo, user_in)
