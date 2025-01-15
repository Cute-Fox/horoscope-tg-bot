import requests
from bs4 import BeautifulSoup

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

print(get_horoscope('libra','monthly'))