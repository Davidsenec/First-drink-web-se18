from pydantic import BaseModel
from app.models.user import UserStatus


class UserRegister(BaseModel):
    user_name: str
    password: str
    full_name: str
    nick_name: str
    contact_info: str
    address : str

class UserLogin(BaseModel):
    user_name: str
    password : str

class UserResponse(BaseModel):
    full_name: str
    nick_name: str
    contact_info: str
    address : str

class AdminResponse(UserResponse):
    status : UserStatus