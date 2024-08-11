class TestPostController:
    def setup_class(self):
        self.url = "/api/posts"

    def test_get_posts_success(self, client):
        response = client.get(self.url)
        assert response.status_code == 200
        response_json = response.json()
        assert response_json == []
