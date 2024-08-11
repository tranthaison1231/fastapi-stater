class TestAuthController:
    def setup_class(self):
        self.url = "/api/register"

    def test_login_fail_with_exist_email(self, client):
        response = client.post(
            self.url,
            json={
                "email": "ttson.1716@gmail.com",
                "password": "test123",
                "username": "test",
            },
        )
        assert response.status_code == 409
        response_json = response.json()
        assert response_json["detail"] == "User with this email already exists"
