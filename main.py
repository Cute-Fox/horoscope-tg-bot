import telebot
import random
import config

bot = telebot.TeleBot(config.api_token)

# Типо данные для гороскопа, цвета и советы
horoscopes = {
    'Овен': 'Сегодня отличный день для новых начинаний!',
    'Телец': 'Будьте осторожны с финансовыми решениями.',
    'Близнецы': 'Сегодня вам предстоит много общаться, используйте этот шанс.',
    'Рак': 'Эмоции будут сильными, постарайтесь сохранять спокойствие.',
    'Лев': 'Время для новых проектов и ярких решений.',
    'Дева': 'Обратите внимание на мелкие детали, они будут важны.',
    'Весы': 'Сегодня хорош день для установления гармонии в отношениях.',
    'Скорпион': 'Не бойтесь быть собой, ваш стиль принесет успех.',
    'Стрелец': 'Постарайтесь не принимать поспешных решений.',
    'Козерог': 'Фокус на долгосрочных целях принесет результат.',
    'Водолей': 'День благоприятен для творческих проектов.',
    'Рыбы': 'День обещает быть спокойным и гармоничным.'
}

colors = {
    'Овен': ['красный', 'оранжевый'],
    'Телец': ['зеленый', 'коричневый'],
    'Близнецы': ['жёлтый', 'синий'],
    'Рак': ['белый', 'серый'],
    'Лев': ['золотой', 'желтый'],
    'Дева': ['серый', 'зелёный'],
    'Весы': ['пастельные оттенки'],
    'Скорпион': ['темно-красный', 'черный'],
    'Стрелец': ['фиолетовый', 'синий'],
    'Козерог': ['темно-зеленый', 'синий'],
    'Водолей': ['голубой', 'мятный'],
    'Рыбы': ['светло-голубой', 'лавандовый']
}

advices = {
    'Овен': 'Сегодня не бойтесь идти на риск.',
    'Телец': 'Слушайте свою интуицию.',
    'Близнецы': 'Не откладывайте на завтра то, что можете сделать сегодня.',
    'Рак': 'Будьте терпимее к другим.',
    'Лев': 'Сделайте первый шаг к вашим целям.',
    'Дева': 'Не переживайте из-за мелочей.',
    'Весы': 'Ищите гармонию в своих делах.',
    'Скорпион': 'Действуйте решительно.',
    'Стрелец': 'Не откладывайте важные дела на потом.',
    'Козерог': 'Терпение и упорство приведут к успеху.',
    'Водолей': 'Будьте открыты новым идеям.',
    'Рыбы': 'Позвольте себе немного отдыха.'
}

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Гороскоп")
    item2 = telebot.types.KeyboardButton("Цвет дня")
    item3 = telebot.types.KeyboardButton("Совет дня")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Привет! 🌟 Я твой личный бот, готов помочь тебе с гороскопом, цветом дня или советом. Выбери, что тебе нужно!", reply_markup=markup)

# Чел выбирает категорию 
@bot.message_handler(func=lambda message: message.text in ['Гороскоп', 'Цвет дня', 'Совет дня'])
def category_choice(message):
    # Запрашиваем сам знак 
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    zodiac_signs = ['Овен ♈️', 'Телец ♉️', 'Близнецы ♊️', 'Рак ♋️', 'Лев ♌️', 'Дева ♍️', 'Весы ♎️', 'Скорпион ♏️', 'Стрелец ♐️', 'Козерог ♑️', 'Водолей ♒️', 'Рыбы ♓️']
    for sign in zodiac_signs:
        markup.add(telebot.types.KeyboardButton(sign))
    bot.send_message(message.chat.id, "Выберите свой знак зодиака, и я расскажу, что вас ждёт!", reply_markup=markup)

    # Запоминаем категорию и переходим к zodiac info
    bot.register_next_step_handler(message, zodiac_info)

def zodiac_info(message):
    try:
        zodiac = message.text.split(' ')[0]  # Получаем знак зодиака
        category = message.text.split(' ')[1]  # Считываем категорию
    except IndexError:
        # Если треш 
        bot.send_message(message.chat.id, "Не удалось понять ваш выбор. Попробуйте снова.")
        return

    # Возвращаем данные для выбранной категории
    if category == 'Гороскоп':
        response = horoscopes.get(zodiac, "Не могу найти гороскоп для этого знака.")
    elif category == 'Цвет дня':
        response = random.choice(colors.get(zodiac, ["Белый"]))
    elif category == 'Совет дня':
        response = advices.get(zodiac, "Просто будь собой!")
    else:
        response = "Неизвестная категория."

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("А у других знаков?")
    markup.add(item1)
    bot.send_message(message.chat.id, f"{response}\n\nВыберите другую категорию:", reply_markup=markup)

bot.polling()