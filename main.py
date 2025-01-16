import telebot
import random
import config
from bs4 import BeautifulSoup
import requests
import magic

bot = telebot.TeleBot(config.api_token)

# Данные для цвета дня и совета
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

advices = {
    'Овен': 'Сегодня не бойтесь идти на риск. 💥🔥',
    'Телец': 'Слушайте свою интуицию. 👂✨',
    'Близнецы': 'Не откладывайте на завтра то, что можете сделать сегодня. ⏳💪',
    'Рак': 'Будьте терпимее к другим. 💖🌿',
    'Лев': 'Сделайте первый шаг к вашим целям. 👣🎯',
    'Дева': 'Не переживайте из-за мелочей. 🍃🌸',
    'Весы': 'Ищите гармонию в своих делах. ⚖️🌈',
    'Скорпион': 'Действуйте решительно. 🦂💥',
    'Стрелец': 'Не откладывайте важные дела на потом. ⏳🔑',
    'Козерог': 'Терпение и упорство приведут к успеху. 🏔️💎',
    'Водолей': 'Будьте открыты новым идеям. 💡🌌',
    'Рыбы': 'Позвольте себе немного отдыха. 🐟🌙'
}

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Гороскоп 🔮")
    item2 = telebot.types.KeyboardButton("Цвет дня 🌈")
    item3 = telebot.types.KeyboardButton("Совет дня ✨")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Привет! 🌟 Я твой личный бот, готов помочь тебе с гороскопом, цветом дня или советом. Выбери, что тебе нужно!", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Гороскоп 🔮', 'Цвет дня 🌈', 'Совет дня ✨'])
def category_choice(message):
    global selected_category
    selected_category = message.text  # Сохраняем выбранную категорию
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    zodiac_signs = ['Овен ♈️', 'Телец ♉️', 'Близнецы ♊️', 'Рак ♋️', 'Лев ♌️', 'Дева ♍️', 'Весы ♎️', 'Скорпион ♏️', 'Стрелец ♐️', 'Козерог ♑️', 'Водолей ♒️', 'Рыбы ♓️']
    for sign in zodiac_signs:
        markup.add(telebot.types.KeyboardButton(sign))
    bot.send_message(message.chat.id, "Выберите свой знак зодиака, и я расскажу, что вас ждёт!", reply_markup=markup)
    bot.register_next_step_handler(message, zodiac_info)

def zodiac_info(message):
    zodiac = message.text.split(' ')[0]  # Извлекаем знак зодиака!!!
    sign_mapping = {
        'Овен': 'aries', 'Телец': 'taurus', 'Близнецы': 'gemini', 'Рак': 'cancer',
        'Лев': 'leo', 'Дева': 'virgo', 'Весы': 'libra', 'Скорпион': 'scorpio',
        'Стрелец': 'sagittarius', 'Козерог': 'capricorn', 'Водолей': 'aquarius', 'Рыбы': 'pisces'
    }
    zodiac_eng = sign_mapping.get(zodiac)

    # Если выбрали "Гороскоп", показываем кнопки для выбора периода, тыкаем
    if selected_category == 'Гороскоп 🔮':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(
            telebot.types.InlineKeyboardButton("На сегодня", callback_data=f"{zodiac_eng}_today"),
            telebot.types.InlineKeyboardButton("На завтра", callback_data=f"{zodiac_eng}_tomorrow"),
            telebot.types.InlineKeyboardButton("На неделю", callback_data=f"{zodiac_eng}_weekly"),
            telebot.types.InlineKeyboardButton("На месяц", callback_data=f"{zodiac_eng}_monthly")
        )
        bot.send_message(message.chat.id, "Выберите период, для которого хотите гороскоп:", reply_markup=markup)
    else:
        # Для "Цвет дня" и "Совет дня" сразу выводим данные, база есть
        if selected_category == 'Цвет дня 🌈':
            color, number = magic.get_day_color_and_number(zodiac)
            response = f"Ваш цвет дня: {color}\nВаше число дня: {number}"
        elif selected_category == 'Совет дня ✨':
            response = magic.get_random_wish_from_json()

        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(telebot.types.KeyboardButton("Вернуться в меню"))
        bot.send_message(message.chat.id, response, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    zodiac_eng = call.data.split('_')[0]
    period = call.data.split('_')[1]
    
    horoscope = magic.get_horoscope(zodiac_eng, period)
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton("Вернуться в меню"))
    bot.send_message(call.message.chat.id, horoscope, reply_markup=markup)

# Обработчик кнопки "Вернуться в меню"; Господи, помоги!!!
@bot.message_handler(func=lambda message: message.text == "Вернуться в меню")
def return_to_menu(message):
    start(message)

bot.polling()