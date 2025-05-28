from unittest.mock import patch

from src.transaction_reader import read_csv
from src.transaction_reader import read_excel


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
