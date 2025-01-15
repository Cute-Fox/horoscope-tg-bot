import requests
from bs4 import BeautifulSoup
import random
import json
from datetime import datetime

def get_horoscope(sign: str, period: str="today") -> str:
    '''
    signs = aries, taurus, gemini, cancer, leo, virgo, libra, scorpio,
            sagittarius, capricorn, aquarius, pisces

    periods = yesterday, today, tomorrow, weekly, monthly, 2025
    '''
    if period == 'today':
        url = f"https://horoscopes.rambler.ru/{sign}/"
    else:
        url = f"https://horoscopes.rambler.ru/{sign}/{period}/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Ошибка: Не удалось получить данные с {url}")
        return None
    
    soup = BeautifulSoup(response.text, "html.parser")
    horoscope = soup.find("p", class_="_5yHoW AjIPq")
    
    if horoscope:
        return horoscope.text.strip()
    else:
        print("Гороскоп не найден.")
        return None

def get_day_color_and_number():
    """Возвращает цвет и число дня, основанные на текущей дате."""
    colors = ["Красный", "Синий", "Зелёный", "Жёлтый", "Фиолетовый", "Оранжевый", "Белый"]
    current_date = datetime.now()
    
    # Число дня — это день месяца
    day_number = current_date.day
    
    # Цвет дня — выбирается на основе дня недели
    day_of_week = current_date.weekday()  # 0 - понедельник, 6 - воскресенье
    day_color = colors[day_of_week]
    
    return day_color, day_number

def get_random_wish_from_json(file_path="wishes.json"):
    """Возвращает случайное пожелание на день из JSON-файла."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            wishes = data.get("wishes", [])
            if not wishes:
                return "Пожеланий пока нет!"
            return random.choice(wishes)
    except (FileNotFoundError, json.JSONDecodeError):
        return "Ошибка: файл с пожеланиями не найден или повреждён."
