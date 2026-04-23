import json
import logging
from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", "a", encoding="utf-8")
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)




def read_json_file(file_path: str) -> List:
    """
      Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
     Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            transactions_list = json.load(file)
            if isinstance(transactions_list, list):
                logger.info(f"Файл {file_path} успешно прочитан.")
                return transactions_list
            else:
                logger.warning(f"Содержимое файла {file_path} не является списком.")
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден.")
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}.")
    return []
# translations_ = read_json_file('data/operation.json')
# print(translations_)

