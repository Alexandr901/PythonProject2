import pytest

from src.widget import mask_account_card
from src.widget import get_date


@pytest.mark.parametrize(
    "user_card, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
    ],
)
def test_mask_account_card(user_card: str, expected: str) -> None:
    assert mask_account_card(user_card) == expected


def test_invalid_mask_account_card() -> None:
    with pytest.raises(ValueError):
        assert mask_account_card("")


@pytest.mark.parametrize(
    "user_date, expected",
    [("2024-03-11T02:26:18.671407", "11.03.2024"), ("1996-08-12T03:25:15.632801", "12.08.1996")],
)
def test_get_date(user_date: str, expected: str) -> None:
    assert get_date(user_date) == expected


def test_invalid_get_date() -> None:
    with pytest.raises(ValueError):
        assert get_date("")
