from abc import ABC, abstractmethod

from app.domain.post.post_model import Post
from app.domain.post.post_schema import PostRequest


class PostRepositoryInterface(ABC):
    @abstractmethod
    async def get_posts(self) -> list[Post]:
        pass

    @abstractmethod
    async def create_post(self, post_request: PostRequest) -> Post:
        pass
