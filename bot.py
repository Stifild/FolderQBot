from random import randint

import telebot
from telebot.types import ReplyKeyboardMarkup

from iop import IOP, Error

clean_markup = telebot.types.ReplyKeyboardRemove()
io = IOP()
er = Error()
user_data = io.user

bot = telebot.TeleBot(token=io.bot_api)


@bot.message_handler(content_types=['text'])
def message_processing(message: telebot.types.Message):
    if message.text == "/start":
        txt, buttons = io.get_quest_message(1)

        bot.send_message(message.chat.id,
                         io.get_quest_description(1),
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
                         text="Oops! There seems to be a error.\n\nsystem integrity ="
                              f" {user_data[str(message.from_user.id)]['hp']}/100")
    if message.text.lower() == "тополь" and user_data[str(message.from_user.id)]["stage"] == 10:
        button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("/start")
        bot.send_message(chat_id=message.chat.id, text="Поздравляю ты прошел_а этот квест!", reply_markup=button)
        user_data[str(message.from_user.id)]["next_error"] = -1
    if user_data[str(message.from_user.id)]["hp"] <= 0:
        button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("/start")
        bot.send_message(chat_id=message.chat.id, text="Вы проиграли", reply_markup=button)
    if message.text == "записка" and user_data[str(message.from_user.id)]['stage'] == 12:
        bot.send_message(chat_id=message.chat.id, text=io.next_note())
    if message.text == "фото" and user_data[str(message.from_user.id)]['stage'] == 13:
        with open(io.next_photo(), "rb") as f:
            bot.send_photo(chat_id=message.chat.id, photo=f)
    elif message.text in io.its_dict.values():
        user_data[str(message.from_user.id)]["stage"] = io.get_int(message.text)
        txt, buttons = io.get_quest_message(user_data[str(message.from_user.id)]['stage'])
        with open(f'media/for msg/{randint(1, 20)}.png', 'rb') as f:
            bot.send_photo(chat_id=message.chat.id, photo=f, caption=txt, reply_markup=buttons)
    user_data[str(message.from_user.id)]["count_of_steps"] += 1
    io.write_json("data/user.json", user_data)


bot.infinity_polling()
