from telebot import TeleBot
from config import *
import chatHandler

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def onStart(message):
    keyboard = chatHandler.stages['language_pref']
    reply_text = chatHandler.texts['onstart']
    bot.send_message(message.chat.id, reply_text, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def onTextMessageRecieved(message):
    #do something with text messages
    pass

bot.polling(none_stop=True)
