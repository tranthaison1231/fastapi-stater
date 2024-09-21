from abc import ABC, abstractmethod


class UploadProviderInterface(ABC):
    @abstractmethod
    def upload(self, file: bytes, file_name: str) -> str:
        pass
