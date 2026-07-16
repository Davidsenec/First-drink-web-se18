from app.dtos.user import UserUpdate, UserResponse
from app.repositories.user_repositories import UserRepository
from app.models.user import User


class UserServices:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def update_info(self, info: UserUpdate, current_user: User) -> UserResponse:
        new_info = self.repo.update_user(current_user, info)
        return new_info
