from unittest.mock import patch

from src.transaction_reader import count_transactions_by_category
from src.transaction_reader import read_csv
from src.transaction_reader import read_excel
from src.transaction_reader import search_transactions_by_description


@patch("pandas.read_csv")
def test_read_csv(mock_read_csv):
    mock_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    mock_df = mock_read_csv.return_value
    mock_df.to_dict.return_value = mock_data
    result = read_csv("mock_path.csv")
    assert result == mock_data


@patch("pandas.read_excel")
def test_read_excel(mock_read_excel):
    mock_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    mock_df = mock_read_excel.return_value
    mock_df.to_dict.return_value = mock_data
    result = read_excel("mock_path.xlsx")
    assert result == mock_data


def test_search_transactions_by_description():
    transactions = [
        {"description": "Покупка в магазине", "amount": 1000},
        {"description": "Перевод другу", "amount": 500},
        {"description": "Оплата коммунальных услуг", "amount": 2000},
    ]
    search_string = "Покупка"
    expected_result = [{"description": "Покупка в магазине", "amount": 1000}]
    assert search_transactions_by_description(transactions, search_string) == expected_result


def test_search_transactions_empty_result():
    transactions = [
        {"description": "Перевод другу", "amount": 500},
        {"description": "Оплата коммунальных услуг", "amount": 2000},
    ]
    search_string = "Покупка"
    expected_result = []
    assert search_transactions_by_description(transactions, search_string) == expected_result


def test_count_transactions_by_category():
    transactions = [
        {"description": "Покупка в магазине", "amount": 1000},
        {"description": "Перевод другу", "amount": 500},
        {"description": "Оплата коммунальных услуг", "amount": 2000},
        {"description": "Покупка продуктов", "amount": 800},
    ]
    categories = ["Покупка", "Перевод", "Оплата"]
    expected_result = {"Покупка": 2, "Перевод": 1, "Оплата": 1}
    assert count_transactions_by_category(transactions, categories) == expected_result


def test_count_transactions_empty_categories():
    transactions = [
        {"description": "Покупка в магазине", "amount": 1000},
        {"description": "Перевод другу", "amount": 500},
    ]
    categories = []
    expected_result = {}
    assert count_transactions_by_category(transactions, categories) == expected_result
