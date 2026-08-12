def test_get_users(client):
    response = client.get('/user/')

    assert response.status_code == 200
    assert response.json() == []
    
def test_create_user(client, user_data):
    
    response = client.post("/user/", json=user_data)
    
    assert response.status_code == 201
    assert response.json()["name"] == user_data["name"]
    assert response.json()["email"] == user_data["email"]
    
def test_get_user(client, user, user_data):

    response = client.get(f"/user/{user['id']}")

    assert response.status_code == 200
    assert response.json()["name"] == user_data["name"]
    assert response.json()["email"] == user_data["email"]
    
def test_update_user(client, user):

    update_data = {
        "name": "Updated User"
    }

    response = client.patch(
        f"/user/{user['id']}",
        json=update_data
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Updated User"
    
def test_update_user_password(client, user, user_data):
    updated_data = {
        "password": "NewPassword123"
    }
    
    response = client.patch(
        f'/user/{user["id"]}', 
        json=updated_data
    )
    
    assert response.status_code == 200
    
    response_login = client.post(
        '/auth/login', 
        json={
            "email": user_data["email"],
            "password": user_data["password"]
        }
    )
    assert response_login.status_code == 401
    
    response_updated_login = client.post(
        '/auth/login', 
        json={
            "email": user_data["email"],
            "password": updated_data["password"]
        }
    )
    assert response_updated_login.status_code == 200
    
    
def test_delete_user(client, user):

    response = client.delete(f"/user/{user['id']}")

    assert response.status_code == 204

    get_response = client.get(f"/user/{user['id']}")

    assert get_response.status_code == 404

def test_get_user_not_found(client):
    response = client.get("/user/999")

    assert response.status_code == 404
    
def test_create_user_duplicate_email(client, user_data):
    
    duplicated_data = user_data.copy()
    duplicated_data['email'] = "duplicate@example.com"

    first_response = client.post("/user/", json=duplicated_data)

    assert first_response.status_code == 201

    second_response = client.post("/user/", json=duplicated_data)

    assert second_response.status_code == 409
    
def test_create_user_missing_email(client, user_data):
    test_data = user_data.copy()
    del test_data['email']

    response = client.post("/user/", json=test_data)

    assert response.status_code == 422
    
def test_create_user_invalid_email(client, user_data):
    test_data = user_data.copy()
    test_data['email'] = "invalid-email"

    response = client.post("/user/", json=test_data)

    assert response.status_code == 422