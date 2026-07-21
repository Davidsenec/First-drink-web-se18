from app.models.user import UserStatus
from fastapi import HTTPException, status
from app.repositories.admin_repositories import AdminRepository


class AdminServices:
    def __init__(self, repo: AdminRepository):
        self.repo = repo

    def edit_status(self, id: int, new_status: UserStatus):
        user = self.repo.check_id(id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Not Found",
            )
        return self.repo.update_status(user, new_status)

    def get_user(self):
        return self.repo.get_all_data()

    def delete(self, id: int):
        user = self.repo.check_id(id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Not Found",
            )
        if user.is_admin:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied.",
            )
        return self.repo.delete_user(user)
