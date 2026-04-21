import os
import requests
from dotenv import load_dotenv
import pytest
import json
from unittest.mock import patch, Mock

load_dotenv()
API_KEY = os.getenv("API_KEY")


def currency_conversion(translation: dict) -> float:
    """
    Функция, осуществляющая конвертацию в рубли
    """
    try:
        amount = float(translation["operationAmount"]["amount"])
        currency = translation["operationAmount"]["currency"]["code"]

        if currency != "USD":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
            payload = {}
            headers = {"apikey": API_KEY}
            response = requests.request("GET", url=url, headers=headers, data=payload)
            status_code = response.status_code
            result = json.loads(response.text)
            amount_rub = float(result['result'])
            if status_code != 200:
                print(f"Ошибка запроса: Код {status_code}, Описание: {result}")
                return 0.0
            return amount_rub
        else:
            return amount
    except Exception as e:
        print(f"Ошибка конвертации: {e}")
        return 0.0


transaction = {
    "operationAmount": {
        "amount": "100.0",
        "currency": {
            "code": "USD"
        }
    }
}


@patch('requests.request')
def test_currency_conversion(mock_request):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = json.dumps({'result': '7500.0'})
    mock_request.return_value = mock_response

    result = currency_conversion(transaction)

    assert result == 7500.0


if __name__ == "__main__":
    pytest.main()
