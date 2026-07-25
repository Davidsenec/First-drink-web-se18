from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.repositories.admin_repositories import AdminRepository
from app.repositories.user_repositories import UserRepository
from app.services.admin_services import AdminServices
from app.services.auth_services import AuthServices
from app.services.user_services import UserServices

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


def get_admin_repo(db: DbSession) -> AdminRepository:
    return AdminRepository(db)


AdminRepositoryDep = Annotated[AdminRepository, Depends(get_admin_repo)]


def get_admin_service(repo: AdminRepositoryDep) -> AdminServices:
    return AdminServices(repo)


AdminServicesDep = Annotated[AdminServices, Depends(get_admin_service)]
