<div id="header" align="left">
  <img src="https://i.gifer.com/7X49.gif"/>
</div>

# [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=800size=45&duration=2000&pause=2000&color=BE0EF7&vCenter=true&width=450&lines=%F0%9F%8C%9F%F0%9F%94%AE+Horoscope+Telegram+Bot++)](https://git.io/typing-svg)

Наш бот делиться с пользователем гороскопом, дает совет дня, а также показывает счастливое число и цвет для знаков зодиака

---

## [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=1200&duration=2000&pause=2000&color=BE0EF7&vCenter=true&width=435&lines=%F0%9F%9A%80+%D0%9A%D0%B0%D0%BA+%D0%BD%D0%B0%D1%87%D0%B0%D1%82%D1%8C+%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%D1%81%D1%8F)](https://git.io/typing-svg)
1. 📥 **Скачайте репозиторий** в рабочую папку:
2. 🛠️ **Устноавите необходимые** библиотеки с помощью команды
```bash
pip install -r requirements.txt
```
3. 📝 **Создайте файл** `config.py` в папке вашего проекта
4. 🔑 Добавьте в `config.py` **API-токен** вашего Telegram-бота в следующем формате
```python
api_token = 'your-api-token-from-tg-father-bot'
```
5. ▶️ **Запустите бота**
```bash
python main.py
```

## [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=1200&duration=2000&pause=2000&color=BE0EF7&vCenter=true&width=435&lines=%F0%9F%8C%8C+%D0%9A%D0%B0%D0%BA+%D1%8D%D1%82%D0%BE+%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D0%B5%D1%82)](https://git.io/typing-svg)
- Бот с помощью библиотеки `BeautifulSoup4` парсит данные с популярного сайта с гороскопами и выводит их пользователю в зависимости от его ЗЗ: 
👉 https://horoscopes.rambler.ru/

- **Счастливый цвет и число** генерируются псевдослучайным образом, основанным на текущей дате. 🗓️

- **Пожелания на день** выбираются случайным образом из файла `wishes.json`. 📖

## [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=1200&duration=2000&pause=2000&color=BE0EF7&vCenter=true&width=435&lines=%F0%9F%8E%A8+%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B8)](https://git.io/typing-svg)
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

## [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=1200&duration=2000&pause=2000&color=BE0EF7&vCenter=true&width=435&lines=%F0%9F%9B%A0%EF%B8%8F+%D0%A1%D1%82%D0%B5%D0%BA+%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B9)](https://git.io/typing-svg)
Для данного проекта был использован ЯП Python, а также такие модули как 
python-telegram-bot-api
BeautifulSoup4
И пр. встроенные модули (все они есть в текстовом файле requirements.txt)

# [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=1200&size=20&duration=2000&pause=2000&color=BE0EF7&vCenter=true&width=435&lines=%D0%9F%D1%80%D0%BE%D0%B5%D0%BA%D1%82+%D0%B1%D1%8B%D0%BB+%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD)](https://git.io/typing-svg)
Командой ChickenCurryians
Кокоревым Семеном и Шевелевым Александром

## [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=1200&size=35&duration=2000&pause=2000&color=BE0EF7&vCenter=true&width=435&lines=%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F+%D1%88%D1%83%D1%82%D0%BE%D1%87%D0%BA%D0%B0)](https://git.io/typing-svg)

![Jokes Card](https://readme-jokes.vercel.app/api?hideBorder)

Всем мяу!
