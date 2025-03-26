from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

# Инициализация
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def viev_top_studnets():
    """
    Возвращает всех пользователей отсортированный по рейтингу в формате:
    {'top_students': {'сосиска': 15, 'saul': 0}}
    """
    response = supabase.table("students").select("*").order("score", desc=True).execute()
    data = response.data
    top = {}
    for i in data:
        top[i['login']] = i['score']
    return {'top_students': top}


def viev_top_teams():
    """
    Возвращает всех пользователей отсортированный по рейтингу в формате:
    {'top_teams': {'Солнечные': 143, 'Сосиски': 52}}
    """
    response = supabase.table("teams").select("*").order("score", desc=True).execute()
    data = response.data
    top = {}
    for i in data:
        top[i['team']] = i['score']
    return {'top_teams': top}
