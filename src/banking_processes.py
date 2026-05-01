import re
from typing import Any, Dict, List
from collections import Counter

def process_bank_search(data:list[dict], search:str)->list[dict]:
    """
    Функция, принимающая список словарей с данными о банковских операциях
    и строку поиска, а возвращает список словарей, у которых в описании есть
    данная строка.
    """
    return [transaction for transaction in data if re.search(search, transaction['description'], flags=re.IGNORECASE)]

def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Функция, которая принимает список словарей с данными о банковских операциях
    и список категорий операций. Возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """
    descriptions = [transaction['description'] for transaction in data]
    filtered_descriptions = [desc for desc in descriptions if desc in categories]
    return dict(Counter(filtered_descriptions))