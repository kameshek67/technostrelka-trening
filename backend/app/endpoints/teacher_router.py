from fastapi import APIRouter, Depends, HTTPException, Security
from app.shemas.users_shemas import RegisterStudent
from app.functions.login_function import registration_student, auth_student
from app.functions.teacher_function import add_score, add_team_task

teacher_router = APIRouter(prefix='/teacher')


@teacher_router.put('/add_point', summary='Зачислить баллы ученику по логину')
def add_point_student(login: str, count_point: int):
    try:
        add_score(login, count_point)
    except Exception:
        return {'detail': 'invalid data'}
    return {'detail': 'success'}

'''Все что дальше пока в разработке, я спать)'''
@teacher_router.post('/add_team_task', summary='Создать задание для команды')
def team_task_add(teams: list, count_point: int):
    return {'detail': 'success'}

@teacher_router.post('/add_team_task', summary='Создать задание для ученика')
def team_task_add(teams: list, count_point: int):
    return {'detail': 'success'}
