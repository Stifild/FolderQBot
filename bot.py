import telebot
import iop
import hulls

clean_markup = telebot.types.ReplyKeyboardRemove()
tout=iop.SaveOutputs

bot = telebot.TeleBot(tout.bot_api)

@bot.message_handler(commands=['start'])
def start(message):
  
