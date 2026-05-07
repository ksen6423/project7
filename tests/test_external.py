import json
from unittest.mock import Mock, patch

import pytest

from src.external_api import currency_conversion

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
