import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def currency_conversion(translation: dict) -> float:
    """
    Функция, осуществляющая конвертацию в рубли
    """
    try:
        amount = float(translation["operationAmount"]["amount"])
        currency = translation["operationAmount"]["currency"]["code"]

        if currency != "RUB":
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
