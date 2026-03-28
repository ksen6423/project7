import pytest


from src.widget import mask_account_card, get_date

def test_length_card(length_card_mask):
    assert mask_account_card([]) == length_card_mask

@pytest.mark.parametrize("value, expected", [
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658")
])

def test_length_card(value, expected):
    assert mask_account_card(value) == expected

    with pytest.raises(TypeError):
        mask_account_card("Visa Platinum 8990922113665229", "Счет 64686473678894779589 ")


def test_length_account(length_account_mask):
    assert mask_account_card([]) == length_account_mask

@pytest.mark.parametrize("value, expected", [
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Счет 65423658971223364411", "Счет **4411")
])

def test_length_account(value, expected):
    assert mask_account_card(value) == expected

    with pytest.raises(TypeError):
        mask_account_card("Счет 64686473678894779589", "MasterCard 7158 30** **** 6758")


def test_date_format(get_date_format):
    assert get_date(formatted_date="2024-03-11T02:26:18.671407") == get_date_format