import telebot
import random
import sqlite3
from telebot import types

# Замените 'YOUR_BOT_TOKEN' на ваш реальный токен, полученный от BotFather
API_TOKEN = '7024818120:AAFmSPU9dBUa9_PbFNoxHM9_BLyhU4HUCJw'

bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML')

# Создание подключения к базе данных SQLite
conn = sqlite3.connect('users.db', check_same_thread=False)
# Создание курсора для выполнения запросов к базе данных
c = conn.cursor()
# Создание таблицы "users" с тремя столбцами: id (автоинкрементный целочисленный), user_id (целочисленный), username (текст)
c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, username TEXT)')
# Сохранение изменений в базе данных
conn.commit()

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Получаем идентификатор пользователя из сообщения
    user_id = message.from_user.id
    # Получаем имя пользователя из сообщения
    username = message.from_user.username

    if username is None:
        username = "Unknown"

    # Проверяем, есть ли уже такой пользователь в базе данных
    c.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = c.fetchone()

    if user is None:
        # Если пользователь не найден, добавляем его в базу данных
        c.execute('INSERT INTO users (user_id, username) VALUES (?, ?)', (user_id, username))
        # Сохраняем изменения в базе данных
        conn.commit()
        print(f"User {user_id} added to the database.")
    else:
        print(f"User {user_id} is already in the database.")


    # создание кнопок
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('/help')
    btn2 = types.KeyboardButton('/rad')
    markup.add(btn1, btn2)

    # отправка сообщения юзеру
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите команду:", reply_markup=markup)

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "<b>Доступные команды:</b>\n"
        "/start - начать взаимодействие с ботом\n"
        "/rad - отправить случайное изображение\n"
        "/help - получить помощь и информацию о командах\n"
    )
    bot.reply_to(message, help_text)

# Обработчик команды /rad
@bot.message_handler(commands=['rad'])
def send_random_image(message):
    # первая колонка
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Кнопка 1', url='https://t.me/+Uuv83tzKFXpkNzMy')
    markup.add(btn1)

    # Вторая и третья кнопки в одной строке под первой кнопкой
    btn2 = types.InlineKeyboardButton('Кнопка 2', url='https://t.me/+Uuv83tzKFXpkNzMy')
    btn3 = types.InlineKeyboardButton('Кнопка 3', url='https://t.me/+Uuv83tzKFXpkNzMy')
    markup.row(btn2, btn3)

    try:
        # Выбираем случайное число от 0 до 9
        random_index = random.randint(0, 5)
        image_path = f"./img/image{random_index}.jpg"
        
        # Отправляем изображение пользователю
        with open(image_path, 'rb') as image_file:
            bot.send_photo(message.chat.id, image_file, reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {e}")

# Обработчик входящих изображений
@bot.message_handler(content_types=['photo', 'video', 'sticker'])
def handle_image(message):
    choice = random.choice(['😍', '👍', '👎', 'Ну такое...']) 
    bot.reply_to(message, choice)

# Обработчик текстовых сообщений
@bot.message_handler()
def handle_unknown_command(message):
    bot.reply_to(message, "<b>Я не хочу разговаривать на эту тему...</b>")

# Запуск бота
bot.polling()