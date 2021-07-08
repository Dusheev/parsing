from logging import info
import telebot
from MyToken import token
from telebot import types
from parsingbot import list1

bot = telebot.TeleBot(token)

entry = {}

inline_keyboard = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton("нажми сюда", callback_data="here")
inline_keyboard.add(btn1)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,"Привет, парсим категорию - НОВОСТИ. ", reply_markup=inline_keyboard)



@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data=='here':
        chat_id=c.message.chat.id
        here_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        k1 = types.KeyboardButton('p1')
        k19 = types.KeyboardButton('Quit')
        here_keyboard.add(k1, k19)
        global msg
        msg = bot.send_message(chat_id,"select p1",reply_markup=here_keyboard)
        bot.register_next_step_handler(msg,get_category_income)
    


def get_category_income(message):
    chat_id=message.chat.id
    entry = message.text
    if entry == "p1":
        print(list1)
        bot.send_message(chat_id, str(list1))
        bot.register_next_step_handler(msg,get_category_income)
    if entry == "Quit":
        bot.send_message(chat_id,"До свидания")


bot.polling()