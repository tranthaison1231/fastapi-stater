from fastapi import APIRouter, Depends, File, UploadFile
from typing_extensions import Annotated

from app.application.use_cases.upload.upload_file import UploadFileUseCase
from app.infrastructure.upload.s3_provider import S3Provider

router = APIRouter(tags=["Upload"])


@router.post("/")
async def upload(
    file: Annotated[UploadFile, File(...)],
    s3_provider: Annotated[S3Provider, Depends()],
):
    upload_file_use_case = UploadFileUseCase(s3_provider)
    return await upload_file_use_case.excute(file)
