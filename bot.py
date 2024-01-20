import telebot
from iop import IOP, Quest, Error
from random import

clean_markup = telebot.types.ReplyKeyboardRemove()
user_data = {}
io = IOP()
q = Quest()
er = Error()

bot = telebot.TeleBot(token=io.bot_api)


@bot.message_handler(content_types=['text'])
def message_procesing(message: telebot.types.Message):
  if message.text == "/start":
    murkup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,
                                               one_time_keyboard=True)
    murkup.add(q.get_quest_buttons(1))

    bot.send_message(message.chat.id,
                     q.get_quest_discription(1),
                     reply_markup=murkup)

    user_data[message.from_user.id] = {
        "username": message.from_user.username,
        "stage": 1,
        "hp": 100,
        "next_error": 0,
    }
    return "new_user"
  elif message.text == "Начать":
    bot.send_photo(chat_id=message.chat.id)
  
  
    
