from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials

from app.application.constants import ErrorMessages
from app.application.dependencies.auth import Auth
from app.application.exceptions import unauthorized_bearer
from app.application.services.jwt_provider import JWTProvider
from app.domain.user.user_model import User
from app.infrastructure.database.repositories.user_repository import UserRepository


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(Auth()),
    user_repository: UserRepository = Depends(),
):
    token = credentials.credentials

    payload = JWTProvider.verify_access_token(token=token)

    if payload is None:
        raise unauthorized_bearer()

    use_id = payload.get("userId")

    if not use_id:
        raise unauthorized_bearer()

    user = await user_repository.get_user(id=use_id)

    if not user:
        raise unauthorized_bearer(ErrorMessages.USER_NOT_FOUND)

    return user


current_user_dependency = Annotated[User, Depends(get_current_user)]
