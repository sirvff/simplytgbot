import telebot
from telebot import types
from telebot import apihelper

bot = telebot.TeleBot('номер бота')




@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Готовься к старту, бот', 'Или не готовься')
    bot.send_message(message.chat.id, 'Всегда готов, go пиши и поехали', reply_markup=keyboard)

@bot.message_handler(commands=['go'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Да', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Нет', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Странно, почему здесь есть выбор?', callback_data=5))
    bot.send_message(message.chat.id, text="Путина любите", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'От старых штиблет')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Заходите, как определитесь')

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Не переживайте, ваше мнение нигде не учитывается. Как обычно')
    answer = ''
    if call.data == '3':
        answer = 'Бог вам судья'
    elif call.data == '4':
        answer = 'А придётся'
    elif call.data == '5':
        answer = 'Ну да, странновато...'

    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

bot.polling()
