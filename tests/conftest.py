import pytest

@pytest.fixture
def length_card():
    return "Номер карты должен содержать 16 цифр"

@pytest.fixture
def mask_card():
    return "2548 78** **** 5689"

@pytest.fixture
def length_account():
    return "Номер счета должен содержать 20 цифр"

@pytest.fixture
def mask_account():
    return "**8912"

@pytest.fixture
def length_card_mask():
    return "Visa Platinum 8990922113665229"

@pytest.fixture
def length_account_mask():
    return "Счет 73654108430135874305"

@pytest.fixture
def get_date_format():
    return "11.03.2024"