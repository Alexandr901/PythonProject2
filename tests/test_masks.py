import pytest

from src.masks import get_mask_card_number
from src.masks import get_mask_account


@pytest.mark.parametrize(
    "card_num, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("4758264516284964", "4758 26** **** 4964"),
        ("9285619274858732", "9285 61** **** 8732"),
    ],
)
def test_get_mask_card_number(card_num: str, expected: str) -> None:
    assert get_mask_card_number(card_num) == expected


def test_invalid_get_mask_card_number() -> None:
    with pytest.raises(ValueError):
        assert get_mask_card_number("")
        assert get_mask_card_number("125125452626136426")
        assert get_mask_card_number("ewqg")


@pytest.mark.parametrize(
    "acc_num, expected",
    [
        ("73654108430135874305", "**4305"),
        ("23566455472347343734", "**3734"),
    ],
)
def test_get_mask_account(acc_num: str, expected: str) -> None:
    assert get_mask_account(acc_num) == expected


def test_invalid_get_mask_account() -> None:
    with pytest.raises(ValueError):
        assert get_mask_account("436")
        assert get_mask_account("weg")
