from fastapi import APIRouter, status
from app.config.security import CurrentAdminDep
from app.config.dependencies import AdminServicesDep
from app.dtos.user import UserStatusUpdate, AdminResponse


router = APIRouter(
    prefix="/admin",
    tags=["admin"],
)


@router.put(
    "/check_in/{id}", status_code=status.HTTP_200_OK, response_model=AdminResponse
)
def check_in(
    id: int,
    current_admin: CurrentAdminDep,
    new_status: UserStatusUpdate,
    service: AdminServicesDep,
):
    return service.edit_status(id, new_status.status)


@router.get(
    "/get_user", status_code=status.HTTP_200_OK, response_model=list[AdminResponse]
)
def admin_get_user(
    current_admin: CurrentAdminDep,
    service: AdminServicesDep,
):
    return service.get_user()


@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    id: int,
    current_admin: CurrentAdminDep,
    service: AdminServicesDep,
):
    return service.delete(id)
