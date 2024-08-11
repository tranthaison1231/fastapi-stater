def test_get_posts(client):
    response = client.get(
        "/api/posts",
    )
    assert response.status_code == 200
    response_json = response.json()
    assert response_json == []
