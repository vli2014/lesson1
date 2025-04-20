import telebot
from config import TOKEN

# Инициализация бота с использованием его токена
bot = telebot.TeleBot(TOKEN)

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, я эхобот, я буду отвечать также как и ты!\
""")
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

# Запуск бота
bot.infinity_polling()
