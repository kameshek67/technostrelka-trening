from pydantic import BaseModel


class RegisterStudent(BaseModel):
    login: str
    password: str
    team: str
    full_name: str
    grade: str