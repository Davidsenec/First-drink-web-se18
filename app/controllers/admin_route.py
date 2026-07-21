from fastapi import APIRouter, status
from app.config.security import CurrentUserDep
from app.config.dependencies import AdminServicesDep
from app.dtos.user import UserStatusUpdate, AdminResponse


router = APIRouter()


@router.put(
    "/admin/check_in/{id}", status_code=status.HTTP_200_OK, response_model=AdminResponse
)
def check_in(
    id: int,
    current_admin: CurrentUserDep,
    new_status: UserStatusUpdate,
    service: AdminServicesDep,
):
    return service.edit_status(id, new_status.status, current_admin)


@router.get(
    "/admin/user", status_code=status.HTTP_200_OK, response_model=list[AdminResponse]
)
def admin_get_user(
    current_admin: CurrentUserDep,
    service: AdminServicesDep,
):
    return service.get_user(current_admin)


@router.delete("/admin/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    id: int,
    current_admin: CurrentUserDep,
    service: AdminServicesDep,
):
    return service.delete(id, current_admin)
