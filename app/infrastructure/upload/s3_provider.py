import boto3

from app.core.config import settings
from app.infrastructure.upload.abstract import UploadProviderInterface


class S3Provider(UploadProviderInterface):
    bucket_name = settings.AWS_BUCKET_NAME

    def __init__(self) -> None:
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION_NAME,
        )

    def upload(self, file: bytes, file_name: str | None):
        self.s3.upload_fileobj(file, self.bucket_name, file_name)

        return f"https://{self.bucket_name}.s3.amazonaws.com/{file_name}"
