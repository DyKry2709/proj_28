from pydantic import BaseModel, constr

class AuthRequestModel(BaseModel):
    username: constr(strict=True)   # Имя пользователя для аутентификации, valid: admin
    password: constr(strict=True)   # Пароль для аутентификации, valid: password123

class AuthResponse(BaseModel):
    token: str