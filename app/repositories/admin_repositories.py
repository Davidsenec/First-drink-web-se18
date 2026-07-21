from sqlalchemy.orm import Session
from app.models.user import User, UserStatus


class AdminRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_data(self):
        user_data = (
            self.db.query(User).filter(User.is_admin.is_(False)).order_by(User.id).all()
        )
        return user_data

    def check_id(self, id: int):
        return self.db.query(User).filter(User.id == id).first()

    def update_status(self, user: User, new_status: UserStatus) -> User:
        user.status = new_status
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, user: User):
        self.db.delete(user)
        self.db.commit()
        return None
