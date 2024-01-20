import json
from dotenv import load_dotenv
from os import getenv
import random

load_dotenv()


class IOP:
  quest: dict
  its_dict: dict
  files: dict
  user: dict
  bot_api = str(getenv('BOT_TOKEN'))
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

  def get_str(self, num: int) -> str:
    return self.its_dict[str(num)]

  def get_int(self, str: str) -> int | None:
    for key, value in self.its_dict.items():
      if value == str:
        return int(key)
    return None


class Quest(IOP):

  def __init__(self) -> None:
    super().__init__()

  def get_quest_discription(self, stage: int) -> dict:
    return self.quest[self.get_str(stage)]["discription"]

  def get_quest_buttons(self, stage: int) -> list:
    return self.quest[self.get_str(stage)]["buttons"]

  def get_file(self, stage: int) -> list | None:
    return self.files[self.get_str(stage)]


class Error:
  damage: int

  def __init__(self) -> None:
    self.damage = random.randint(1, 20)

  def get_next_error(self) -> int:
    return random.randint(1, 10)