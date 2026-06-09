# 🚀 Backend Control Users with JWT and Token

API REST desenvolvida com **FastAPI** para gerenciamento de usuários,
incluindo autenticação com **JWT**, hash de senha e estrutura modular
seguindo boas práticas de backend.

> ⚠️ Projeto em desenvolvimento --- novas funcionalidades serão
> adicionadas.

------------------------------------------------------------------------

## 📌 Funcionalidades atuais

-   ✅ Cadastro de usuários
-   🔐 Hash de senha com `passlib (bcrypt)`
-   📋 Listagem de usuários
-   🧠 Estrutura organizada em camadas (routes, services, models)
-   ⚙️ Validação com Pydantic
-   🚀 API com FastAPI

------------------------------------------------------------------------

## 🛠️ Tecnologias utilizadas

-   Python 3.10+
-   FastAPI
-   Uvicorn
-   Pydantic
-   Passlib (bcrypt)
-   Python-JOSE (JWT - em progresso)

------------------------------------------------------------------------

## 📂 Estrutura do projeto

    backend-control-users-with_jwt_and_token/
    │
    ├── main.py
    ├── database.py
    │
    ├── models/
    │   └── user.py
    │
    ├── routes/
    │   └── user_routes.py
    │
    ├── services/
    │   ├── user_services.py
    │   └── security_handler.py
    │
    └── requirements.txt

------------------------------------------------------------------------

## 🧠 Arquitetura

ROUTE → SERVICE → (UTILS / DATABASE)

------------------------------------------------------------------------

## ⚙️ Como rodar o projeto

``` bash
git clone https://github.com/seu-usuario/seu-repo.git
cd backend-control-users-with_jwt_and_token
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

------------------------------------------------------------------------

## 📡 Endpoints

### ➕ Criar usuário

POST /user/

### 📋 Listar usuários

GET /users

------------------------------------------------------------------------

## 🔐 Segurança

-   Senhas com hash usando bcrypt
-   Nunca armazenadas em texto puro

------------------------------------------------------------------------

## ⚠️ Melhorias futuras

-   JWT completo
-   Banco de dados real
-   Testes
-   Docker

------------------------------------------------------------------------

## 👨‍💻 Autor

Thiago 🚀
