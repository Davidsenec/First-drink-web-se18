from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.repositories.user_repositories import UserRepository
from app.services.user_services import UserServices
from app.services.auth_services import AuthServices

DbSession = Annotated[Session, Depends(get_db)]


def get_user_repo(db: DbSession) -> UserRepository:
    return UserRepository(db)


UserRepositoryDep = Annotated[UserRepository, Depends(get_user_repo)]


def get_user_service(repo: UserRepositoryDep) -> UserServices:
    return UserServices(repo)


UserServiceDep = Annotated[UserServices, Depends(get_user_service)]


def get_auth_service(repo: UserRepositoryDep) -> AuthServices:
    return AuthServices(repo)


AuthServicesDep = Annotated[AuthServices, Depends(get_auth_service)]
