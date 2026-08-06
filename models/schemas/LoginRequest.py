from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    email: EmailStr = Field(
        ...,
        description="User email address",
        examples=["thiago@email.com"]
    )

    password: str = Field(
        ...,
        description="User password",
        examples=["StrongPassword123"]
    )