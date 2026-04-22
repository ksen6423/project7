import pytest
import json
import unittest
from unittest.mock import mock_open, patch
from src.utils import read_json_file


mock_file = mock_open(read_data=
    '[{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",'
    ' "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},'
    ' "description": "Перевод организации", "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"}]')

@patch("builtins.open", mock_file)
def test_read_json_file() -> None:
    with patch("json.load", return_value=None) as mock_load:
        assert read_json_file("./data/operations.json") == []


