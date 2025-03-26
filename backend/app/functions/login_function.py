from supabase import create_client
from backend.config import SUPABASE_URL, SUPABASE_KEY

# Инициализация
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def registration_student(login: str, password: str, team: str, full_name: str, grade: str):
    data = {'login': login, 'password': password, 'team': team,
            'full_name': full_name, 'grade': grade}
    supabase.table("students").insert(data).execute()


def auth_student(login: str, password: str):
    response = supabase.table("students").select("*").eq("password", password).eq('login', login).execute()
    return response.data
