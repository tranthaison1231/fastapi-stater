import time

from app.config import settings

from jose import JWTError, jwt


class JWTProvider:
    @staticmethod
    def create_access_token(data: dict, expires_delta: int = 3600):
        to_encode = data.copy()

        to_encode.update({"exp": time.time() + expires_delta})

        return jwt.encode(
            to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM
        )

    @staticmethod
    def verify_access_token(token: str):
        try:
            decoded_token = jwt.decode(
                token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM]
            )

            return decoded_token if decoded_token["exp"] >= time.time() else None

        except JWTError:
            return None
