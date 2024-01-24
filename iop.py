import json
import random
from os import getenv

from dotenv import load_dotenv
from telebot import types

load_dotenv()


class IOP:
    """Класс обработки операций ввода и вывода"""
    quest: dict
    its_dict: dict
    files: dict
    user: dict
    bot_api = str(getenv('BOT_TOKEN'))
    text: dict
    note_progress = 0
    photo_progress = 0

    def get_json(self, path: str) -> dict:
        """Функция, которая загружает данные из файла и возвращает словарь.
              Если файла нет, то возвращается пустой словарь.
              :param path: Путь к файлу с данными
              :return: Словарь с данными пользователей
              """
        try:
            with open(path, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def __init__(self) -> None:
        self.quest = self.get_json("data/quest.json")
        self.its_dict = self.get_json("data/IntToStr.json")
        self.files = self.get_json("data/files.json")
        self.user = self.get_json("data/user.json")
        self.text = self.get_json("data/text.json")

    def write_json(self, path: str, data: dict) -> None:
        """Функция, которая сохраняет данные в файл.
              :param data: Словарь с данными пользователей
              :param path: Путь к файлу с данными
              """
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def get_str(self, num: int) -> str | None:
        """Функция перевода чисел в строки по словарю перевода.
        Если этой пары нет, то возвращается None.
            :param num: Число
            :return: Строка или None
        """
        try:
            return self.its_dict[str(num)]
        except KeyError:
            return None

    def get_int(self, str: str) -> int | None:
        """
        Функция перевода строки в число по словарю перевода.
        Если этой пары нет, то возвращается None.
        :param str: Строка
        :return: Число или None
        """
        for key, value in self.its_dict.items():
            if value == str:
                return int(key)
        return None

    def get_quest_description(self, stage: int) -> str:
        """
        Функция получения сообщения под картинкой.
        :param stage: Этап
        :return: Текст
        """
        return self.quest[self.get_str(stage)]["description"]

    def get_quest_buttons(self, stage: int) -> list:
        """
        Функция получения списка с кнопками для сообщения.
        :param stage: Этап
        :return: Список
        """
        return self.quest[self.get_str(stage)]["buttons"]

    def get_file(self, stage: int) -> list | None:
        """Функция получения списка с текстом для файлов в квесте
        :param stage: Этап
        :return: Список
        """
        try:
            return self.files[self.get_str(stage)]
        except KeyError:
            return None

    def get_quest_message(self, stage: int) -> str and types.ReplyKeyboardMarkup:
        """
        Функция для собирания переменных текста под картинкой и кнопки.
        :param stage: Этап
        :return: Строка с текстом и кнопки
        """
        message = self.get_quest_description(stage)
        buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for i in self.get_quest_buttons(stage):
            buttons.add(i)
        return message, buttons

    def next_photo(self):
        """
        Функция получения пути для фото
        :return: Путь
        """
        self.note_progress += 1
        if self.note_progress >= 0:
            self.note_progress = 0
        return self.get_file(13)[self.note_progress]

    def next_note(self) -> str:
        """
        Функция получения записки
        :return: Записка
        """
        self.note_progress += 1
        if self.note_progress >= 10:
            self.note_progress = 0
        return self.get_file(12)[self.note_progress]


class Error:
    """
    Класс ошибок
    """
    damage: int

    def __init__(self) -> None:
        self.damage = random.randint(-20, 50)

    def get_next_error(self) -> int:
        """
        Функция получения количества шагов до следующий ошибки
        :return: Число ошибок
        """
        return random.randint(1, 10)
