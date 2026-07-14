from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.repositories.user_repositories import UserRepository
from app.services.UserServices import Userservices
from app.dtos.user import UserResponse, UserUpdate

router = APIRouter()


def get_user_repo(db: Session = Depends(get_db)):
    return UserRepository(db)


@router.put(
    "/Edit_Info/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=UserResponse
)
def Update_Info(
    id: int, info: UserUpdate, repo: UserRepository = Depends(get_user_repo)
):
    return Userservices.updatate_info(repo, id, info)
