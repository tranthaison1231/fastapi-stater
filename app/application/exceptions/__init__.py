from fastapi import HTTPException, status


def unauthorized_basic() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Basic"},
    )


def unauthorized_bearer(
    msg: str = "Invalid authorization credentials",
) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=msg,
        headers={"WWW-Authenticate": "Bearer"},
    )


def bad_request(msg: str = "Bad request.") -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=msg,
    )


def forbidden(
    msg: str = "You don't have permission to access this resource",
) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=msg,
        headers={"WWW-Authenticate": "Bearer"},
    )


def not_found(msg: str = "Resource not found.") -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=msg,
    )


def conflict(msg: str = "Resource already exists.") -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=msg,
    )


def internal_server_error(msg: str = "Internal server error.") -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=msg,
    )


def expired_token(msg: str = "Token has expired.") -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=msg,
        headers={"WWW-Authenticate": "Bearer"},
    )


def unprocessable_entity(msg: str = "Unprocessable entity.") -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=msg,
    )
