import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_length_card(length_card):
    assert get_mask_card_number([]) == length_card



@pytest.mark.parametrize("value, expected", [
    ("1234567891234567", "1234 56** **** 4567"),
    ("3256893256893256", "3256 89** **** 3256"),
    ("9874563219874564", "9874 56** **** 4564")
])
def test_mask_card(value, expected):
    assert get_mask_card_number(value) == expected

    with pytest.raises(TypeError):
        get_mask_card_number("1236456987412356", "123456** **** 4567")


def test_length_account(length_account):
    assert get_mask_account([]) == length_account

@pytest.mark.parametrize("value, expected", [
    ("12345678912345678912", "**8912"),
    ("32165498732165498732", "**8732"),
    ("95286395286395286395", "**6395")
])

def test_mask_account(value, expected):
    assert get_mask_account(value) == expected

    with pytest.raises(TypeError):
        get_mask_account("12345678912345678912", "**25369")