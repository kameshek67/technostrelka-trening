from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_KEY

# Инициализация
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)




def delete_student(login: str):
    supabase.table('students').delete().eq('login', login).execute()


def get_students_by_grade(grade: int):
    return supabase.table("students").select("*").eq("grade", grade).execute()
