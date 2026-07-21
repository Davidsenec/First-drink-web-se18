from fastapi import APIRouter, status
from app.config.dependencies import UserServiceDep
from app.config.security import CurrentUserDep
from app.dtos.user import UserResponse, UserUpdate

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.put("/edit_info", status_code=status.HTTP_200_OK, response_model=UserResponse)
def update_info(
    info: UserUpdate, current_user: CurrentUserDep, service: UserServiceDep
):
    return service.update_info(info, current_user)


@router.get("/me", status_code=status.HTTP_200_OK, response_model=UserResponse)
def get_current_user(current_user: CurrentUserDep):
    return current_user
