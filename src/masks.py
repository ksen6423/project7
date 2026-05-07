# import logging

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# file_handler = logging.FileHandler("../logs/masks.log", "a", encoding="utf-8")
# formatter = logging.Formatter('%(asctime)s %(name)s - %(levelname)s: %(message)s')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер банковской карты"""
    result = ""
    if len(card_number) != 16:
        result = "Номер карты должен содержать 16 цифр"
        # logger.info("Пользователь указал меньше цифр, чем нужно")
    else:
        result = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return result


print(get_mask_card_number(card_number="2542586214555689"))


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер банковского счета"""
    result = ""
    if not isinstance(account_number, str):
        account_number = str(account_number)
    if len(account_number) != 20:
        result = "Номер счета должен содержать 20 цифр"
        # logger.info("Пользователь указал больше цифр, чем нужно")
    else:
        result = f"**{account_number[-4:]}"
    return result


print(get_mask_account(account_number="12345678912345678912"))
