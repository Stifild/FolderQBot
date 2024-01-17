import telebot
from iop import IOP

clean_markup = telebot.types.ReplyKeyboardRemove()
user_data = {}
io = IOP

bot = telebot.TeleBot(token=io.bot_api)


@bot.message_handler(content_types=['text'])
def message_procesing(message: telebot.types.Message):
  if message.text == "/start":
    bot.send_message(message.chat.id,
                     io.text[message.from_user.language_code]['start'],
                     reply_markup=clean_markup)
    #todo доделать
    user_data[message.from_user.id]={
      "username": message.from_user.username,
      "language": message.from_user.language_code
    }
    
    
