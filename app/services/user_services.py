from app.dtos.user import UserResponse, UserUpdate
from app.models.user import User
from app.repositories.user_repositories import UserRepository


class UserServices:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def update_info(self, info: UserUpdate, current_user: User) -> UserResponse:
        new_info = self.repo.update_user(current_user, info)
        return new_info
