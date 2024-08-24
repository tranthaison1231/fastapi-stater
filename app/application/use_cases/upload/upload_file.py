from uuid import uuid4

import magic
from fastapi import Depends, UploadFile

from app.application.constants import ErrorMessages
from app.application.exceptions import bad_request, internal_server_error
from app.infrastructure.upload.s3_provider import S3Provider

KB = 1024
MB = 1024 * KB
SUPPORTED_FILE_TYPES = {"image/jpeg": "jpeg", "image/png": "png"}


class UploadFileUseCase:
    def __init__(self, s3_provider: S3Provider = Depends()) -> None:
        self.s3_provider = s3_provider

    async def excute(self, file: UploadFile):
        try:
            contents = await file.read()
            file_size = len(contents)

            if not 0 < file_size <= 1 * MB:
                raise bad_request(ErrorMessages.LIMIT_FILE_SUPPORT)

            file_type = magic.from_buffer(contents, mime=True)

            if file_type not in SUPPORTED_FILE_TYPES:
                raise bad_request(ErrorMessages.NOT_SUPPORT_FILE_TYPES)

            file_name = f"{uuid4()}.{SUPPORTED_FILE_TYPES[file_type]}"

            url = self.s3_provider.upload(file=contents, file_name=file_name)

            return {"url": url}
        except Exception as e:
            raise internal_server_error(str(e))
