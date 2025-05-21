import os
import requests
from dotenv import load_dotenv

load_dotenv()

def convert_to_rub(transaction: dict) -> float:
    """Конвертирует сумму транзакции в рубли.

    Args:
        transaction (dict): Словарь с данными о транзакции, содержащий
                            'amount' и 'currency'.

    Returns:
        float: Сумма транзакции в рублях.
    """
    amount = transaction["amount"]
    currency = transaction["currency"]

    if currency == "RUB":
        return float(amount)

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": os.getenv("API_KEY")}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return float(response.json()["result"])
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        raise ValueError("Ошибка при получении курса валюты") from e