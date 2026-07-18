from app.models.user import User, UserStatus
from fastapi import HTTPException, status
from app.repositories.admin_repositories import AdminRepository


class AdminServices:
    def __init__(self, repo: AdminRepository):
        self.repo = repo

    def edit_status(self, id: int, new_status: UserStatus, current_admin: User):
        if not current_admin.is_admin:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        user = self.repo.check_id(id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Not Found",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return self.repo.update_status(user, new_status)

    def get_user(self, current_admin: User):
        if not current_admin.is_admin:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return self.repo.get_all_data()
