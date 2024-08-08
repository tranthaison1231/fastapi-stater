from modules.router import api_router
from fastapi import FastAPI
from fastapi.responses import UJSONResponse


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="FastAPI Starter Project",
        description="FastAPI Starter Project",
        version="1.0",
        docs_url="/docs/",
        redoc_url="/redoc/",
        openapi_url="/openapi.json",
        default_response_class=UJSONResponse,
    )

    app.include_router(router=api_router, prefix="/api")

    return app
