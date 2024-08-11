from app.presentation.rest import api_router
from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.utils.signleton import singleton


@singleton
class AppCreator:
    def __init__(self):
        self.app = FastAPI(
            title="FastAPI Starter Project",
            description="FastAPI Starter Project",
            version="1.0",
            docs_url="/docs/",
            redoc_url="/redoc/",
            openapi_url="/openapi.json",
            default_response_class=UJSONResponse,
        )

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        self.app.include_router(router=api_router, prefix="/api")


app_creator = AppCreator()
app = app_creator.app
