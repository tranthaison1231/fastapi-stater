class TestAuthController:
    @staticmethod
    def test_register_fail_with_exist_email(client):
        response = client.post(
            "/api/register",
            json={
                "email": "ttson.1716@gmail.com",
                "password": "test123",
                "username": "test",
            },
        )
        assert response.status_code == 409
        response_json = response.json()
        assert response_json["detail"] == "User with this email already exists"

    @staticmethod
    def test_login_success(client):
        response = client.post(
            "/api/login",
            json={
                "email": "ttson.1716@gmail.com",
                "password": "test123",
            },
        )
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["access_token"] is not None
        assert response_json["refresh_token"] is not None
