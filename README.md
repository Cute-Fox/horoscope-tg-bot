# 🌟 Horoscope Telegram Bot 🔮

Наш бот делиться с пользователем гороскопом, дает совет дня, а также показывает счастливое число и цвет для знаков зодиака

---

## 🚀 Как начать пользоваться
1. 📥 **Скачайте репозиторий** в рабочую папку:
2. 🛠️ **Устноавите необходимые** библиотеки с помощью команды
```bash
pip install -r requirements.txt
```
3. 📝 **Создайте файл** `config.py` в папке вашего проекта
4. 🔑 Добавьте в `config.py` **API-токен** вашего Telegram-ботавашего телеграма в следующем формате
```python
api_token = '7763050590:AAGlapJMGAgLfBuSdLcLfznjNCka1a06b74'
```
5. ▶️ **Запустите бота**
```bash
python main.py
```

## 🌌 Как это работает
* Бот с помощью библиотеки `BeautifulSoup4` парсит данные с популярного сайта с гороскопами и выводит их пользователю в зависимости от его ЗЗ: 
👉 https://horoscopes.rambler.ru/

**Счастливый цвет и число** генерируются псевдослучайным образом, основанным на текущей дате. 🗓️

**Пожелания на день** выбираются случайным образом из файла `wishes.json`. 📖

## 🎨 Настройки
### Параметры цветов, а также пожелания вы можете настроит под себя
1. **Для настройки цветов** необходимо изменять словарь `colors`:
```python
colors = {
        'Овен': ['красный ❤️', 'оранжевый 🧡', 'розовый 🌸'],
        'Телец': ['зеленый 🍃', 'коричневый 🍂', 'песочный 🌾'],
        'Близнецы': ['жёлтый 💛', 'синий 💙', 'бирюзовый 🌊'],
        'Рак': ['белый 🤍', 'серый 🐘', 'бежевый 🍂'],
        'Лев': ['золотой ✨', 'желтый 🌟', 'медный 🪙'],
        'Дева': ['серый 🌫️', 'зелёный 🌿', 'лавандовый 💜'],
        'Весы': ['пастельные оттенки 🌸', 'пудровый 🌷'],
        'Скорпион': ['темно-красный 🍷', 'черный 🖤', 'бордовый 🍒'],
        'Стрелец': ['фиолетовый 💜', 'синий 🌌', 'пурпурный 🌺'],
        'Козерог': ['темно-зеленый 🌲', 'синий 🌀', 'серебристый 🪙'],
        'Водолей': ['голубой 🌊', 'мятный 🍃', 'аквамариновый 🌊'],
        'Рыбы': ['светло-голубой 🌤️', 'лавандовый 💐', 'розовато-фиолетовый 🟣']
    }
```
⚠️ Важно: у каждого знака зодиака должно быть строго 3 цвета.
2. **Для того чтобы изменить пожелания** достаточно добавить или убрать строки в `wishes.json`. Вы также можете создать свой json файл со своими предсказаниями, просто используйте следующий формат и назовите файл `wishes.json`
```json
{
    "wishes": [
        "First exmp",
        "Second exmp"
    ]
}
```

## 🛠️ Стек технологий
Для данного проекта был использован ЯП Python, а также такие модули как 
python-telegram-bot-api
BeautifulSoup4
И пр. встроенные модули (все они есть в текстовом файле requirements.txt)

# Проект был создан
Командой ChickenCurryians
Кокоревым Семеном и Шевелевым Александром

Всем мяу!