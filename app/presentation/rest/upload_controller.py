from fastapi import APIRouter, Depends, File, UploadFile
from typing_extensions import Annotated

from app.application.use_cases.upload.upload_file import UploadFileUseCase

router = APIRouter(tags=["Upload"])


@router.post("/")
async def upload(
    file: Annotated[UploadFile, File(...)],
    upload_file_use_case: Annotated[UploadFileUseCase, Depends()],
):
    return await upload_file_use_case.excute(file)
