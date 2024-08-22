from fastapi import Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.application.exceptions import unauthorized_bearer
from app.infrastructure.authentication.jwt_provider import JWTProvider


class Auth(HTTPBearer):
    def __init__(self, auto_error: bool = True) -> None:
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        credentials = await super().__call__(request)

        self._validate_credentials(credentials)

        return credentials

    @staticmethod
    def _validate_credentials(credentials: HTTPAuthorizationCredentials | None) -> None:
        if credentials is None or credentials.scheme != "Bearer":
            raise unauthorized_bearer()

        if JWTProvider.verify_access_token(token=credentials.credentials) is None:
            raise unauthorized_bearer()
