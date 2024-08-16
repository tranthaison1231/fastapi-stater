from fastapi import APIRouter, Depends, File, UploadFile
from app.application.use_cases.upload.upload_file import UploadFileUseCase

router = APIRouter(tags=["Upload"])


@router.post("/")
async def upload(
    file: UploadFile = File(...),
    upload_file_use_case: UploadFileUseCase = Depends(),
):
    return await upload_file_use_case.excute(file)
