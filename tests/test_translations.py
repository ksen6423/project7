import os
import unittest
from unittest.mock import mock_open, patch
from src.file_operations import reading_csv_file

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

PATH_TO_FILE_CSV = os.path.join(ROOT_DIR, "data", "C:/Users/cfif/PycharmProjects/PythonProject8/data/transactions (1).csv")


class TestInfoBankOperations(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='id;state;date;amount;currency_name;currency_code;from;to;description\n1;'
                                                              'EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n')
    def test_valid_read_csv(self):
        result = reading_csv_file(PATH_TO_FILE_CSV)
        expected_result = [{
            "id": "1",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации"
        }]
        self.assertEqual(reading_csv_file(result, expected_result))

if __name__ == " --main__":
    unittest.main()
