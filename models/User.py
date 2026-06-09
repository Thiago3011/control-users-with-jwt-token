from pydantic import BaseModel, EmailStr, Field
from datetime import timezone, datetime

class User(BaseModel):
    id: int | None = None
    name: str
    email: EmailStr
    phone: str
    password: str
    status: bool = True
    creation_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))