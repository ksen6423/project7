
def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер банковской карты"""
    result = ""
    if len(card_number) != 16:
        result = "Номер карты должен содержать 16 цифр"
    else:
        result = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return result

print(get_mask_card_number(card_number="2548786214555689"))


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер банковского счета"""
    result = ""
    if len(account_number) != 20:
        result = "Номер счета должен содержать 20 цифр"
    else:
        result = f"**{account_number[-4:]}"
    return result

print(get_mask_account(account_number="12345678912345678912"))

