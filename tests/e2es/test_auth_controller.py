def test_login(client):
    response = client.post(
        "/api/register",
        json={
            "email": "ttson.1714@gmail.com",
            "password": "test123",
            "username": "test",
        },
    )
    assert response.status_code == 409
    response_json = response.json()
    assert response_json["detail"] == "User with this email already exists"
