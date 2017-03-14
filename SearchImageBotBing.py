import logging
import telebot
from py_bing_search import PyBingImageSearch

# Выводим на экран название программы и автора
print('telegramBot by mioe')
print('xubuntu-16.04-amd64')
print('---')

# Создадим переменную bot, в которой будет храниться токен для подключения к боту
bot = telebot.TeleBot('275348962:AAHUWy9lrm5qDM9A9zbLqCRaTJxg8TgrFFY')

# API Key BingSearch
BingKey = "0uZ5Rifm4B3PxJM2P5tCAq0O+PglqlVbylG+2PiUP/M"

@bot.message_handler(commands=['start'])
def SendInfo(message):
    bot.send_message(message.chat.id, 'Привет! я твой бот. Введи запрос для поиска изображения:')

@bot.message_handler(commands=['help'])
def SendHelp(message):
    bot.send_message(message.chat.id, "Список доступных команд: /start, /help")

@bot.message_handler(content_types='text')
def SendMessage(message):
    bot.send_message(message.chat.id, "Ожидайте, мы ищем для Вас картиночки!")
    bot.send_message(message.chat.id, "bing ..")
    bing_image = PyBingImageSearch(BingKey, str(message.text))
    result = bing_image.search(limit=5, format='json')
    for image in result:
        bot.send_photo(message.chat.id, image.media_url)

if __name__== '__main__':
    # Сконфигурируем log-файл
    logging.basicConfig(filename='botLog.log',
                        format='%(filename)s[LINE:%(lineno)d]# '
                               '%(levelname)-8s [%(asctime)s]  '
                               '%(message)s',
                        level=logging.DEBUG)

    logging.info('Start the bot.')

    # В случае возникновения ошибки в log-файл
    # будет добавлена информация и перезапущен бот
    try:
        bot.polling(none_stop=True)
    except Exception:
        logging.critical('ERROR...')
    finally:
        bot.polling(none_stop=True)