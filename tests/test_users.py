def test_get_users(client):
    response = client.get('/user/')

    assert response.status_code == 200
    assert response.json() == []
    
def test_create_user(client):
    user_data = {
        "name": "Test User",
        "email": "test@example.com",
        "phone": "1599999999",
        "password": "password"
    }
    
    response = client.post("/user/", json=user_data)
    
    assert response.status_code == 201
    assert response.json()["name"] == "Test User"
    assert response.json()["email"] == "test@example.com"
    
def test_get_user(client):
    user_data = {
        "name": "Test User",
        "email": "getuser@example.com",
        "phone": "15999999999",
        "password": "StrongPassword123"
    }

    create_response = client.post("/user/", json=user_data)

    user_id = create_response.json()["id"]

    response = client.get(f"/user/{user_id}")

    assert response.status_code == 200
    assert response.json()["name"] == "Test User"
    assert response.json()["email"] == "getuser@example.com"
    
def test_update_user(client):
    user_data = {
        "name": "Test User",
        "email": "update@example.com",
        "phone": "15999999999",
        "password": "StrongPassword123"
    }

    create_response = client.post("/user/", json=user_data)

    user_id = create_response.json()["id"]

    update_data = {
        "name": "Updated User"
    }

    response = client.patch(
        f"/user/{user_id}",
        json=update_data
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Updated User"
    
def test_delete_user(client):
    user_data = {
        "name": "Test User",
        "email": "delete@example.com",
        "phone": "15999999999",
        "password": "StrongPassword123"
    }

    create_response = client.post("/user/", json=user_data)

    user_id = create_response.json()["id"]

    response = client.delete(f"/user/{user_id}")

    assert response.status_code == 204

    get_response = client.get(f"/user/{user_id}")

    assert get_response.status_code == 404

def test_get_user_not_found(client):
    response = client.get("/user/999")

    assert response.status_code == 404
    
def test_create_user_duplicate_email(client):
    user_data = {
        "name": "Test User",
        "email": "duplicate@example.com",
        "phone": "15999999999",
        "password": "StrongPassword123"
    }

    first_response = client.post("/user/", json=user_data)

    assert first_response.status_code == 201

    second_response = client.post("/user/", json=user_data)

    assert second_response.status_code == 409
    
def test_create_user_missing_email(client):
    user_data = {
        "name": "Test User",
        "phone": "15999999999",
        "password": "StrongPassword123"
    }

    response = client.post("/user/", json=user_data)

    assert response.status_code == 422
    
def test_create_user_invalid_email(client):
    user_data = {
        "name": "Test User",
        "email": "invalid-email",
        "phone": "15999999999",
        "password": "StrongPassword123"
    }

    response = client.post("/user/", json=user_data)

    assert response.status_code == 422