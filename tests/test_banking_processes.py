import pytest
from src.banking_processes import process_bank_search, process_bank_operations

@pytest.fixture
def data_():
    return [
        {'description': 'Food'},
        {'description': 'Transport'},
        {'description': 'Food'},
        {'description': 'Entertainment'},
        {'description': 'Payment to John'},
        {'description': 'Transfer to bank'},
        {'description': 'Payment to Jane'},
    ]

@pytest.mark.parametrize(
    "description_word, data_frm",
    [
       ("Payment", [{'description': 'Payment to Jane'},{'description': 'Payment to John'}]),
       ("payment", [{'description': 'Payment to Jane'},{'description': 'Payment to John'}]),
       ("Groceries", []),
       ([], []),
    ],
)
def test_process_bank_search(data_, description_word, data_frm):
    result = process_bank_search(data_, description_word)
    assert result == data_frm

@pytest.fixture
def data_():
    return [
        {'description': 'Food'},
        {'description': 'Transport'},
        {'description': 'Food'},
        {'description': 'Entertainment'},
        {'description': 'Payment to John'},
        {'description': 'Transfer to bank'},
        {'description': 'Payment to Jane'},
    ]

@pytest.mark.parametrize(
    "categories_lst, categories_lst_frm",
    [
        (['Food', 'Transport', 'Entertainment'], {'Food': 2, 'Transport': 1, 'Entertainment': 1}),
        (['Groceries', 'Travel'], {}),
        ([], {}),
        ],
)

def test_process_bank_operations(data_, categories_lst, categories_lst_frm):
    result = process_bank_operations(data_, categories_lst)
    assert result == categories_lst_frm


def test_empty_transactions_list():
    data = []
    categories = ['Food', 'Transport']
    result = process_bank_operations(data, categories)
    assert result == {}