from app.models.user import User
from app.dtos.user import UserUpdate, UserResponse
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def check_user(self, username: str):
        return self.db.query(User).filter(User.user_name == username).first()

    def check_id(self, id: int):
        return self.db.query(User).filter(User.id == id).first()

    def add_user(self, user_in: User):
        self.db.add(user_in)
        self.db.commit()
        self.db.refresh(user_in)

    def update_user(self, user_in_db: User, info: UserUpdate) -> UserResponse:
        user_in_db.full_name = info.full_name
        user_in_db.nick_name = info.nick_name
        user_in_db.contact_info = info.contact_info
        user_in_db.address = info.address
        self.db.commit()
        self.db.refresh(user_in_db)
        return user_in_db
