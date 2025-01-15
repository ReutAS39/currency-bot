import telebot

from bot.config import *
from bot.extensions import Converter, APIException

bot = telebot.TeleBot(settings.BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def greeting(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \
    <в какую валюту перевести>  \
    <количество переводимой валюты>\n Доступные валюты: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for currency in currencys.keys():
        text = '\n'.join((text, currency,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):

    try:
        argums = message.text.split()

        if len(argums) != 3:
            raise APIException('Неверное количество параметров!')

        base, quote, amount = argums
        total_quote = Converter.get_price(base, quote, amount)
        text = f'Цена {amount} {base} в {quote} - {total_quote}'
        bot.send_message(message.chat.id, text)
    except APIException as e:
        bot.reply_to(message, f'Ошибка в команде:\n{e}')


bot.polling(none_stop=True)
