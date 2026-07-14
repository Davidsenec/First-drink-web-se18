from app.dtos.user import UserUpdate, UserResponse
from app.repositories.user_repositories import UserRepository
from fastapi import HTTPException


class Userservices:
    def updatate_info(repo: UserRepository, id: int, info: UserUpdate) -> UserResponse:
        check = repo.check_id(id)
        if not check:
            raise HTTPException(
                status_code=401,
                detail="invalid Id",
                headers={"WWW-Authenticate": "Bearer"},
            )
        new_info = repo.update_user(check, info)
        return new_info
