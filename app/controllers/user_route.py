from fastapi import APIRouter, status
from app.config.dependencies import UserServiceDep
from app.config.security import CurrentUserDep
from app.dtos.user import UserResponse, UserUpdate

router = APIRouter()


@router.put(
    "/edit_info/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=UserResponse
)
def update_info(
    id: int, info: UserUpdate, current_user: CurrentUserDep, service: UserServiceDep
):
    return service.update_info(id, info, current_user)
