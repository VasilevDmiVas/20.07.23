# def tempate_opration(_operation):
#     if operation == '+':
#         return lambda _number1, _number2: f'{_number1} + {_number2} = {_number1 + _number2}'
#     elif operation == '-':
#         return lambda _number1, _number2: f'{_number1} - {_number2} = {_number1 - _number2}'
#     elif operation == '*':
#         return lambda _number1, _number2: f'{_number1} * {_number2} = {_number1 * _number2}'
#     elif operation == '**':
#         return lambda _number1, _number2: f'{_number1}  в степени {_number2} = {_number1 ** _number2}'
#     elif operation == '/' and number2 == 0:
#         print('На ноль делить нельзя')
#     else:
#         return lambda _number1, _number2: f'{_number1} / {_number2} = {_number1 / _number2}'
#
# operation = input('Введите операцию +,-,*,/, ** возведение в степень \n')
# number1 = int(input('Введите первое число\n'))
# number2 = int(input('Введите второе число либо степень\n'))
#
# func_calc = tempate_opration(operation)
# result = func_calc(number1, number2)
# print(result)
# BotFather

import datetime
import telebot
API_TOKEN = '5977535317:AAGCtuq2Xmz5NbiOruJ5Arg4QguM2mwAQoE'
bot = telebot.TeleBot(API_TOKEN)
time1 = datetime.datetime.now()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет всем')
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Для помощи обратитесь к администратору')
@bot.message_handler(commands=['echo'])
def send_welcome(message):
    bot.reply_to(message, 'Привет всем')

@bot.message_handler(commands=['date'])
def send_date(message):
    date_now = time1.strftime('%Y.%m.%d')
    bot.reply_to(message, f'Сегодняшний день {date_now}')

@bot.message_handler(commands=['time'])
def send_time(message):
    time_now = time1.strftime('%H:%M:%S')
    bot.reply_to(message, f'Время сейчас = {time_now}')

@bot.message_handler(content_types=['text'])
def send_text(message):
    message_txt = str(message.text.lower())
    bot.reply_to(message, f'Время сейчас = {time_now}')
bot.infinity_polling()

content_types - любой текст команада