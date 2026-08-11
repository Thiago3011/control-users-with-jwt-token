from datetime import datetime, timezone, timedelta
from jose import jwt
from services.token_handler import SECRET_KEY, ALGORITHM

def test_login(client):
    user_data = {
        "name": "Auth User",
        "email": "auth@example.com",
        "phone": "15999999999",
        "password": "StrongPassword123"
    }

    create_response = client.post("/user/", json=user_data)

    assert create_response.status_code == 201

    login_data = {
        "email": "auth@example.com",
        "password": "StrongPassword123"
    }

    response = client.post("/auth/login", json=login_data)

    assert response.status_code == 200

    response_data = response.json()

    assert "token" in response_data
    assert response_data["token_type"] == "bearer"
    assert response_data["token"]

def test_get_me(client):
    user_data = {
        "name": "Auth User",
        "email": "me@example.com",
        "phone": "15999999999",
        "password": "StrongPassword123"
    }

    create_response = client.post("/user/", json=user_data)

    assert create_response.status_code == 201

    login_response = client.post(
        "/auth/login",
        json={
            "email": "me@example.com",
            "password": "StrongPassword123"
        }
    )

    assert login_response.status_code == 200

    token = login_response.json()["token"]

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    assert response.json()["email"] == "me@example.com"
    
def test_login_wrong_password(client):
    user_data = {
        "name": "Auth User",
        "email": "wrongpassword@example.com",
        "phone": "15999999999",
        "password": "StrongPassword123"
    }

    create_response = client.post("/user/", json=user_data)

    assert create_response.status_code == 201

    response = client.post(
        "/auth/login",
        json={
            "email": "wrongpassword@example.com",
            "password": "WrongPassword123"
        }
    )

    assert response.status_code == 401
    
def test_login_user_not_found(client):
    response = client.post(
        "/auth/login",
        json={
            "email": "notfound@example.com",
            "password": "StrongPassword123"
        }
    )

    assert response.status_code == 401
    
def test_get_me_invalid_token(client):
    response = client.get(
        "/auth/me",
        headers={
            "Authorization": "Bearer invalid-token"
        }
    )

    assert response.status_code == 401
    
def test_get_me_expired_token(client):
    expiration_time = datetime.now(timezone.utc) - timedelta(seconds=1)

    expired_token = jwt.encode(
        {
            "user_id": 1,
            "exp": expiration_time
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": f"Bearer {expired_token}"
        }
    )

    assert response.status_code == 401