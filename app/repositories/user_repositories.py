from app.models.user import User
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self,db:Session):
        self.db = db

    def check_user(self,username:str):
        return self.db.query(User).filter(User.user_name==username).first()
    
    def add_user(self,user_in:User):
        self.db.add(user_in)
        self.db.commit()
        self.db.refresh(user_in)

