from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from app.config.dependencies import AuthServicesDep
from app.dtos.user import UserLogin, UserRegister, UserResponse

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post(
    "/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse
)
def register(user_in: UserRegister, service: AuthServicesDep):
    return service.register(user_in)


@router.post("/login")
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    service: AuthServicesDep,
):
    user_in = UserLogin(user_name=form_data.username, password=form_data.password)
    return service.login(user_in)
