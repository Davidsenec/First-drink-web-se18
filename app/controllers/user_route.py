from fastapi import APIRouter, status
from app.config.dependencies import UserServiceDep
from app.config.security import CurrentUserDep
from app.dtos.user import UserResponse, UserUpdate

router = APIRouter()


@router.put("/edit_info", status_code=status.HTTP_200_OK, response_model=UserResponse)
def update_info(
    info: UserUpdate, current_user: CurrentUserDep, service: UserServiceDep
):
    return service.update_info(info, current_user)
