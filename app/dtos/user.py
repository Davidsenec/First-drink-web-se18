from pydantic import BaseModel, ConfigDict, Field

from app.models.user import UserStatus


class UserRegister(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    user_name: str = Field(
        ..., min_length=3, max_length=50, pattern=r"^[a-zA-Z0-9_-]+$"
    )
    password: str = Field(..., min_length=8, max_length=128)
    full_name: str = Field(..., min_length=1, max_length=100)
    nick_name: str = Field(..., min_length=1, max_length=50)
    contact_info: str = Field(..., min_length=1, max_length=100)
    address: str = Field(..., min_length=1, max_length=255)


class UserLogin(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    user_name: str = Field(..., min_length=1, max_length=50)
    password: str = Field(..., min_length=1, max_length=128)


class UserUpdate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    full_name: str = Field(..., min_length=1, max_length=100)
    nick_name: str = Field(..., min_length=1, max_length=50)
    contact_info: str = Field(..., min_length=1, max_length=100)
    address: str = Field(..., min_length=1, max_length=255)


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_name: str
    full_name: str
    nick_name: str
    contact_info: str
    address: str
    is_admin: bool


class AdminResponse(UserResponse):
    status: UserStatus


class UserStatusUpdate(BaseModel):
    status: UserStatus
