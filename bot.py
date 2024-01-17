import telebot
import iop
import hulls

clean_markup = telebot.types.ReplyKeyboardRemove()
io=iop.IOP

bot = telebot.TeleBot(io.bot_api)

@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, io.text[message]['start'], reply_markup=clean_markup)
