from datetime import datetime, timezone, timedelta
from jose import jwt
from services.token_handler import SECRET_KEY, ALGORITHM

def test_login(client, user_data, user):

    login_data = {
        "email": user_data["email"],
        "password": user_data["password"]
    }

    response = client.post("/auth/login", json=login_data)

    assert response.status_code == 200

    response_data = response.json()

    assert "token" in response_data
    assert response_data["token_type"] == "bearer"
    assert response_data["token"]

def test_get_me(client, user_data, auth_user):

    token = auth_user["token"]

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    assert response.json()["email"] == user_data["email"]
    
def test_login_wrong_password(client, user_data, user):

    response = client.post(
        "/auth/login",
        json={
            "email": user_data["email"],
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