from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

# Инициализация
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def add_score(login: str, points: int):
    current = supabase.table("students").select("score").eq("login", login).execute()

    if not current.data:
        raise ValueError("Пользователь не найден")

    add_points = current.data[0]["score"] + points
    supabase.table("students").update({"score": add_points}).eq("login", login).execute()


def add_student_task(login: str, title: str, task: str, points: int, type: str):
    """
    Принимает данные задания и для какого пользователя оно создано
    """
    data = {"student": login, "title": title, "task": task, "score": points, "type": type}
    supabase.table("students_tasks").insert(data).execute()


def add_team_task(teams: list, title: str, task: str, points: int, type: str):
    """
    Принимает данные задания и для какой команды оно создано
    """
    data = {"teams": teams, "title": title, "task": task, "score_count": points, "type": type}
    supabase.table("team_tasks").insert(data).execute()
