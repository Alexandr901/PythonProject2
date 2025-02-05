from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(user_card: str) -> str:
    """Маскирует карты или счета"""

    if "Счет" in user_card:
        return "Счет " + get_mask_account(user_card)
    else:
        mask_cart_numb = f"{user_card[:-16]}{get_mask_card_number(user_card[-16:])}"
        return mask_cart_numb


def get_date(user_date: str) -> str:
    """Преобразует формат даты"""
    return f"{user_date[8:10]}.{user_date[5:7]}.{user_date[:4]}"
