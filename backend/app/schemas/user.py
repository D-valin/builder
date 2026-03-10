from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

# Schema compartido
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    is_active: Optional[bool] = True
    role: Optional[str] = "CAJERO"

# Registro de usuario (entrada)
class UserCreate(UserBase):
    password: str

# Actualizacion de usuario (entrada)
class UserUpdate(BaseModel):
    id: int
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    role: Optional[str] = None

# Respuesta de usuario (salida)
class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Esquemas para recuperacion de password
class PasswordResetRequest(BaseModel):
    email: EmailStr

class PasswordReset(BaseModel):
    token: str
    new_password: str
