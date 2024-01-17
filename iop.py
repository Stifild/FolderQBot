import json
from dotenv import load_dotenv
from os import getenv

load_dotenv()


def get_json(path: str) -> dict:
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


def write_json(path: str, data: dict) -> None:
  """Функция, которая сохраняет данные в файл.
        :param data: Словарь с данными пользователей
        :param path: Путь к файлу с данными
        """
  with open(path, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)


class SaveOutputs:
  quest = get_json("data/quest.json")
  files = get_json("data/files.json")
  user = get_json("data/user.json")
  bot_api = getenv('BOT_TOKEN')
