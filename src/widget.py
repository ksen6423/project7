import src.masks

def mask_account_card(card_and_account: str | int) -> str:
    """Функция, которая обрабатывает информацию о картах и счетах"""
    account_card_split = card_and_account.split()

    for i, word in enumerate(account_card_split):
        if word.isdigit():

            if len(word) == 20:
                account_card_split[i] = src.masks.get_mask_account(word)
            if len(word) ==16:
                account_card_split[i] = src.masks.get_mask_card_number(word)
        account_card_view = ' '.join(account_card_split)
    return account_card_view
print(mask_account_card(f"Visa Platinum 8990922113665229"))
print(mask_account_card(f"Счет 64686473678894779589"))
print(mask_account_card(f"Maestro 1596837868705199"))
print(mask_account_card(f"MasterCard 7158300734726758"))
print(mask_account_card(f"Счет 35383033474447895560"))
print(mask_account_card(f"Visa Classic 6831982476737658"))
print(mask_account_card(f"Счет 73654108430135874305"))
print(mask_account_card(f"Visa Gold 5999414228426353"))

import re

def get_date(formatted_date: str) -> str:
    """Функция, которая преобразует дату"""

    date_split_list = formatted_date.split('T')
    date_format = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3.\2.\1", (date_split_list[0]))
    return date_format
print(get_date("2024-03-11T02:26:18.671407"))
