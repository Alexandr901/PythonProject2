def filter_by_currency(transactions, currency):
    """Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start, end):
    """Генерирует номера карт в заданном диапазоне."""
    for number in range(start, end + 1):
        card_number = f"{number:016d}"
        formatted_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_number