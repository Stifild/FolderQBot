import json

from dotenv import load_dotenv
from os import getenv

load_dotenv()


class IOP:
  quest: dict
  files: dict
  user: dict
  bot_api = getenv('BOT_TOKEN')
  text: dict

  def load_media(self, path: str):
    with open(path, 'r') as f:
      return f

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
