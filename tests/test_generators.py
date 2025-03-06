import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


def test_filter_by_currency(transactions):
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 3
    assert {t["id"] for t in usd_transactions} == {939719570, 142264268, 895315941}

    rub_transactions = list(filter_by_currency(transactions, "RUB"))
    assert len(rub_transactions) == 2
    assert {t["id"] for t in rub_transactions} == {873106923, 594226727}

    empty_transactions = list(filter_by_currency([], "USD"))
    assert len(empty_transactions) == 0

    no_currency_transactions = list(filter_by_currency(transactions, "GBP"))
    assert len(no_currency_transactions) == 0


def test_transaction_descriptions(transactions):
    descriptions = list(transaction_descriptions(transactions))
    assert len(descriptions) == 5

    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert descriptions == expected_descriptions

    empty_descriptions = list(transaction_descriptions([]))
    assert len(empty_descriptions) == 0


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (5, 5, ["0000 0000 0000 0005"]),
        (99999999, 100000000, ["0000 0000 9999 9999", "0000 0001 0000 0000"]),
        (100, 102, ["0000 0000 0000 0100", "0000 0000 0000 0101", "0000 0000 0000 0102"]),
    ],
)
def test_card_number_generator(start, end, expected):
    generated_numbers = list(card_number_generator(start, end))
    assert generated_numbers == expected

    assert list(card_number_generator(99999999, 100000000)) == ["0000 0000 9999 9999", "0000 0001 0000 0000"]
    assert list(card_number_generator(1, 0)) == []
