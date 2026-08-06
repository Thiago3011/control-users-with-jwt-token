from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str = Field(
        ...,
        description="User full name",
        examples=["Thiago Henrique"]
    )

    email: EmailStr = Field(
        ...,
        description="User email address",
        examples=["thiago@email.com"]
    )

    phone: str = Field(
        ...,
        description="User phone number",
        examples=["+55 15 99999-9999"]
    )

    password: str = Field(
        ...,
        description="User password",
        examples=["StrongPassword123"]
    )


class UserUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        description="User full name",
        examples=["Thiago Henrique"]
    )

    email: EmailStr | None = Field(
        default=None,
        description="User email address",
        examples=["thiago@email.com"]
    )

    phone: str | None = Field(
        default=None,
        description="User phone number",
        examples=["+55 15 99999-9999"]
    )

    password: str | None = Field(
        default=None,
        description="User password",
        examples=["StrongPassword123"]
    )

    status: bool | None = Field(
        default=None,
        description="User account status",
        examples=[True]
    )