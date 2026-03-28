from datetime import datetime
from typing import List

def filter_by_state(list_dictionaries, state: str='EXECUTED'):
    """Функция, которая принимает список словарей и опционально значение для ключа
    (по умолчанию 'EXECUTED')
    и возвращает новый список словарей, содержащих только те словари, у которых ключ
    state соответствует указанному значению.
    """
    dicts_state = []
    for dict_state in list_dictionaries:
        if dict_state.get('state') == state:
            dicts_state.append(dict_state)
    return dicts_state


# print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))


def sort_by_date(list_dictionaries: list[dict], reverse_order: bool = True) -> list[dict]:
    """Функция, которая принимает список словарей и необязательный параметр, задающий
    порядок сортировки (по умолчанию - убывание) и возвращает новый список, отсортированный по дате (date)
    """
    return sorted(
        list_dictionaries,
        key=lambda x: datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=reverse_order)

print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
