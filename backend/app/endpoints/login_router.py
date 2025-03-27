from fastapi import APIRouter, Depends, HTTPException, Security
from backend.app.shemas.users_shemas import RegisterStudent
from backend.app.functions.login_function import registration_student, auth_student

login_router = APIRouter()


@login_router.post("/registration", summary='Регистрация ученика')
def login_student(student_data: RegisterStudent):
    """
    Принимаются данные школьника. Возвращается сообщение с результатом запроса
    по типу {detail: success}
    """
    try:
        registration_student(student_data.login, student_data.password, student_data.team,
                                        student_data.full_name, student_data.grade)
    except Exception:
        return {'detail': 'invalid data'}

    return {'detail': 'success'}


@login_router.post("/authorization", summary='Авторизация ученика')
def authorization_student(login: str, password: str):
    """
    Принимаются данные школьника. Возвращается сообщение с результатом запроса
    по типу {detail: success}
    """
    response = auth_student(login, password)

    if len(response) >= 1:
        return {'detail': 'success'}

    return {'detail': 'invalid data'}
