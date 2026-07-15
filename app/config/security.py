from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import Depends, HTTPException, status
from app.config.dependencies import UserRepositoryDep, AuthServicesDep
from app.models.user import User

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/login")


def get_current_user(
    token: Annotated[str, Depends(oauth2_bearer)],
    repo: UserRepositoryDep,
    service: AuthServicesDep,
) -> User:

    payload = service.check_jwt(token)
    username = payload.get("sub")
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="user not valid",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = repo.check_user(username)
    if not username:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


CurrentUserDep = Annotated[User, Depends(get_current_user)]
