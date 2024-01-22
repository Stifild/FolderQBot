from random import randint

import telebot

from fs import Notes
from iop import IOP, Quest, Error, Message

clean_markup = telebot.types.ReplyKeyboardRemove()
user_data = {}
io = IOP()
q = Quest()
notes = Notes()
er = Error()
msg = Message()
user_data = io.user

bot = telebot.TeleBot(token=io.bot_api)


@bot.message_handler(content_types=['text'])
def message_processing(message: telebot.types.Message):
    if message.text == "/start":
        txt, buttons = msg.get_quest_message(1)

        bot.send_message(message.chat.id,
                         q.get_quest_description(1),
                         reply_markup=buttons)

        user_data[str(message.from_user.id)] = {
            "username": message.from_user.username,
            "stage": 2,
            "hp": 100,
            "next_error": 10,
            "count_of_steps": 0,
            "count_of_error": 0,
        }

    if user_data[str(message.from_user.id)]["next_error"] == user_data[str(message.from_user.id)]["count_of_steps"]:
        user_data[str(message.from_user.id)]["hp"] -= er.damage
        user_data[str(message.from_user.id)]["next_error"] = er.get_next_error()
        user_data[str(message.from_user.id)]["count_of_steps"] = 0
        bot.send_message(chat_id=message.chat.id,
                         text=f"Oops! There seems to be a error.\n\nsystem integrity = {user_data[str(message.from_user.id)]['hp']}/100")

    if message.text == "Тополь" and user_data[str(message.from_user.id)]["stage"] == '10':
        bot.send_message(chat_id=message.chat.id, text="Поздравляю ты прошел_а этот квест!")
    if message.text == "записка" and user_data[str(message.from_user.id)]['stage'] == 12:
        bot.send_message(chat_id=message.chat.id, text=notes.next_note())
    if user_data[str(message.from_user.id)]["hp"] <= 0:
        bot.send_message(chat_id=message.chat.id, text="Вы проиграли")
        user_data.pop(str(message.from_user.id))
    elif message.text in io.its_dict.values():
        user_data[str(message.from_user.id)]["stage"] = io.get_int(message.text)
        txt, buttons = msg.get_quest_message(user_data[str(message.from_user.id)]['stage'])
        with open(f'media/for msg/{randint(1, 20)}.png', 'rb') as f:
            bot.send_photo(chat_id=message.chat.id, photo=f, caption=txt, reply_markup=buttons)
    user_data[str(message.from_user.id)]["count_of_steps"] += 1
    io.write_json("data/user.json", user_data)


bot.infinity_polling()
