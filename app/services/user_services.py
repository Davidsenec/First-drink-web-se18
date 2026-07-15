from app.dtos.user import UserUpdate, UserResponse
from app.repositories.user_repositories import UserRepository
from fastapi import HTTPException, status


class UserServices:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def update_info(self, id: int, info: UserUpdate, current_user) -> UserResponse:
        if id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                detail="Not Allowed",
                headers={"WWW-Authenticate": "Bearer"},
            )
        check = self.repo.check_id(id)
        if not check:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="invalid Id",
                headers={"WWW-Authenticate": "Bearer"},
            )
        new_info = self.repo.update_user(check, info)
        return new_info
