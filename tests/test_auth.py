def test_register(client):
    response = client.post(
        "/auth/register",
        json={
            "email": "pytest@test.com",
            "password": "12345678",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["email"] == "pytest@test.com"
    assert "id" in data
    assert "hashed_password" not in data
