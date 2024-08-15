from datetime import datetime, timedelta

from app.config import settings

from jose import JWTError, jwt


class JWTProvider:
    async def create_access_token(self, data: dict, expires_delta: int = 3600):
        to_encode = data.copy()

        expire = datetime.utcnow() + timedelta(seconds=expires_delta)

        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm="HS256")

        return encoded_jwt

    async def verify_access_token(self, token: str):
        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
            return payload
        except JWTError:
            return None
