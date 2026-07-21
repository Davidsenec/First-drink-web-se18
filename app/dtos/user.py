from pydantic import BaseModel, ConfigDict
from app.models.user import UserStatus


class UserRegister(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    user_name: str
    password: str
    full_name: str
    nick_name: str
    contact_info: str
    address: str


class UserLogin(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    user_name: str
    password: str


class UserUpdate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    full_name: str
    nick_name: str
    contact_info: str
    address: str


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_name: str
    full_name: str
    nick_name: str
    contact_info: str
    address: str


class AdminResponse(UserResponse):
    status: UserStatus


class UserStatusUpdate(BaseModel):
    status: UserStatus
