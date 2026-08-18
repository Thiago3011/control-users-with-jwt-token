# 🚀 User Management API

A REST API built with **FastAPI** for user management and JWT-based authentication.

The project was developed with a modular backend architecture, focusing on **separation of concerns, security, validation, automated testing, and maintainable code**.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.136.3-009688?logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![Pytest](https://img.shields.io/badge/Pytest-Test%20Suite-green?logo=pytest)
![Coverage](https://img.shields.io/badge/Coverage-98%25-brightgreen)

---

## 📌 Features

* 👤 User CRUD
* 🔐 JWT-based authentication
* 🔑 Password hashing with bcrypt
* 🛡️ Protected authentication route with Bearer tokens
* ✅ Request validation with Pydantic
* ⚠️ Centralized HTTP exception handling
* 🔄 Partial user updates with `PATCH`
* 📋 Proper HTTP status codes
* 🧩 Modular service-based architecture
* 📚 Automatic OpenAPI / Swagger documentation
* 🧪 Automated tests with Pytest
* 📊 **98% application code coverage**
* ✅ 16 automated tests
* ✅ Invalid and expired JWT handling

---

## 🛠️ Tech Stack

| Technology           | Purpose                       |
| -------------------- | ----------------------------- |
| **Python**           | Backend language              |
| **FastAPI**          | REST API framework            |
| **SQLAlchemy**       | ORM and database access       |
| **SQLite**           | Development and test database |
| **Pydantic**         | Data validation and schemas   |
| **Python-JOSE**      | JWT creation and validation   |
| **Passlib / bcrypt** | Password hashing              |
| **Pytest**           | Automated testing             |
| **pytest-cov**       | Code coverage                 |
| **Uvicorn**          | ASGI server                   |

---

## 🏗️ Architecture

The project follows a layered architecture designed to keep responsibilities separated:

```text
Client
  │
  ▼
Routes
  │
  ▼
Services
  │
  ├── Authentication
  ├── User operations
  ├── Token handling
  └── User lookup / formatting
  │
  ▼
SQLAlchemy / Database
```

### Main responsibilities

* **Routes** → HTTP endpoints and request dependencies
* **Services** → Business logic
* **Models** → Database models and request schemas
* **Security handlers** → Password hashing and verification
* **Token handler** → JWT generation and validation
* **User finder / formatter** → Reusable user-related operations and response formatting
* **Exception handlers** → Standardized API error responses

---

## 📂 Project Structure

```text
backend-control-users-with_jwt_and_token/
│
├── main.py
├── database.py
├── pytest.ini
├── .coveragerc
│
├── exceptions/
│   └── handlers.py
│
├── models/
│   ├── db/
│   │   └── user.py
│   │
│   └── schemas/
│       ├── LoginRequest.py
│       └── User.py
│
├── routes/
│   ├── user_routes.py
│   └── login_routes.py
│
├── services/
│   ├── auth_services.py
│   ├── formatter.py
│   ├── security_handler.py
│   ├── token_handler.py
│   ├── user_finder.py
│   └── user_services.py
│
└── tests/
    ├── conftest.py
    ├── test_auth.py
    └── test_users.py
```

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd backend-control-users-with_jwt_and_token
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows

```powershell
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the API

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

The Swagger interface can be used to test all endpoints directly from the browser.

---

## 📡 API Endpoints

### 👤 Users

| Method   | Endpoint          | Description    | Status |
| -------- | ----------------- | -------------- | ------ |
| `GET`    | `/user/`          | List all users | `200`  |
| `GET`    | `/user/{user_id}` | Get user by ID | `200`  |
| `POST`   | `/user/`          | Create a user  | `201`  |
| `PATCH`  | `/user/{user_id}` | Update user    | `200`  |
| `DELETE` | `/user/{user_id}` | Delete user    | `204`  |

### 🔐 Authentication

| Method | Endpoint      | Description                        | Status |
| ------ | ------------- | ---------------------------------- | ------ |
| `POST` | `/auth/login` | Authenticate user and generate JWT | `200`  |
| `GET`  | `/auth/me`    | Get the authenticated user         | `200`  |

---

## 🔐 Authentication Flow

Authentication is handled using JWT Bearer tokens.

```text
POST /auth/login
        │
        ▼
Validate credentials
        │
        ▼
Generate JWT
        │
        ▼
Client receives token
        │
        ▼
Authorization: Bearer <token>
        │
        ▼
GET /auth/me
```

Invalid or expired tokens return:

```http
401 Unauthorized
```

The API also handles invalid credentials and non-existent users without exposing sensitive authentication details.

---

## 🛡️ Security

The project implements several security-related practices:

* Passwords are hashed before being stored.
* Passwords are never returned by the API.
* JWT tokens are validated before accessing protected routes.
* Expired JWT tokens are rejected.
* Invalid JWT tokens return `401 Unauthorized`.
* Authentication failures return generic credential errors.
* Request data is validated through Pydantic schemas.

> **Note:** This project is intended for learning and portfolio purposes. Production deployments should use environment variables for secrets and a production-grade database configuration.

---

## 🧪 Automated Testing

The project includes automated tests using **Pytest**.

Current test coverage includes:

* User creation
* User listing
* User retrieval
* User update
* Password update
* User deletion
* Non-existent users
* Duplicate emails
* Missing required fields
* Invalid email validation
* Successful login
* Invalid credentials
* Non-existent users during authentication
* Valid JWT authentication
* Invalid JWT tokens
* Expired JWT tokens

### Run the test suite

```bash
pytest
```

The project is configured so that Pytest automatically runs the test suite and displays code coverage.

### Current results

```text
16 tests passed
98% application code coverage
0 warnings
```

---

## 🧪 Test Isolation

The test suite uses a dedicated **in-memory SQLite database**.

This keeps the test environment isolated from the development database and allows each test to run independently.

The project also uses Pytest fixtures to provide:

* Test HTTP client
* Test database session
* Reusable user data
* Pre-created users
* Authenticated users

---

## 📊 Code Coverage

Coverage is measured using `pytest-cov`.

```bash
pytest
```

The current application coverage is:

```text
98%
```

The remaining uncovered statements are related to application initialization and database dependency setup rather than untested business logic.

---

## 📋 Example Login Request

```json
{
  "email": "user@example.com",
  "password": "StrongPassword123"
}
```

### Successful response

```json
{
  "user_name": "Test User",
  "token_type": "bearer",
  "token": "eyJ..."
}
```

---

## ❌ Error Handling

The API uses appropriate HTTP status codes for different scenarios:

| Status | Scenario                            |
| ------ | ----------------------------------- |
| `200`  | Successful request                  |
| `201`  | Resource successfully created       |
| `204`  | Resource successfully deleted       |
| `401`  | Invalid credentials or JWT          |
| `404`  | Resource not found                  |
| `409`  | Duplicate resource / email conflict |
| `422`  | Request validation error            |

---

## 🚧 Future Improvements

Possible next steps for the project:

* PostgreSQL for production environments
* Environment-based configuration
* Docker / Docker Compose
* CI/CD pipeline
* Refresh tokens
* Pagination and filtering
* More granular authorization / roles
* Production deployment
* API monitoring and logging

---

## 👨‍💻 Author

**Thiago Henrique**

Software Engineer focused on backend development, APIs and Python.

---
