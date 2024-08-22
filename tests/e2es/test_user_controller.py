class TestUserPostController:
    @staticmethod
    def test_get_me_fail_when_not_authenticated(client):
        response = client.get("/api/users/me")
        assert response.status_code == 403
        response_json = response.json()
        assert response_json["detail"] == "Not authenticated"

    @staticmethod
    def test_get_users_success(client):
        response = client.get("/api/users")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json == [
            {
                "id": "62053a02248a49e0b716bf68b3df1176",
                "created_at": "2024-08-11T09:27:44.475553Z",
                "updated_at": "2024-08-11T09:27:44.475556Z",
                "name": "Son Tran",
                "email": "ttson.1740@gmail.com",
            },
            {
                "id": "ec06a396d6964f25bcafcd21e95b8569",
                "created_at": "2024-08-11T09:43:18.721404Z",
                "updated_at": "2024-08-11T09:43:18.721409Z",
                "name": "test",
                "email": "ttson.1714@gmail.com",
            },
            {
                "id": "fcf201fb3ac948c68f37ad337aff0990",
                "created_at": "2024-08-11T10:25:37.128835Z",
                "updated_at": "2024-08-11T10:25:37.128839Z",
                "name": "test",
                "email": "ttson.1715@gmail.com",
            },
            {
                "id": "cd3b89e219b54f85a382f020df707348",
                "created_at": "2024-08-11T10:30:05.000767Z",
                "updated_at": "2024-08-11T10:30:05.000771Z",
                "name": "test",
                "email": "ttson.1716@gmail.com",
            },
            {
                "id": "8e80422210184d8f926bb9f93b2c9fbd",
                "created_at": "2024-08-15T16:40:13.806246Z",
                "updated_at": "2024-08-15T16:40:13.806253Z",
                "name": "tranthaison1231",
                "email": "ttson.1720@gmail.com",
            },
            {
                "id": "e669849625164f0b984891247b937d59",
                "created_at": "2024-08-22T12:46:43.252135Z",
                "updated_at": "2024-08-22T12:46:43.252138Z",
                "name": "sontran",
                "email": "son.tran1719@gmail.com",
            },
            {
                "id": "3deb3f129d4d404a8167e0fcd4c6cfeb",
                "created_at": "2024-08-22T12:50:00.000548Z",
                "updated_at": "2024-08-22T12:50:00.000551Z",
                "name": "sontran",
                "email": "ttson.1723@gmail.com",
            },
        ]
