from src.masks import get_mask_account, get_mask_card_number



def mask_account_card(user_card: str) -> str:
    """Функция маскировки карты или счета"""

    if "Счет" in user_card:
        return "Счет " + get_mask_account(user_card)
    else:
        mask_cart_numb = f"{user_card[:-16]}{get_mask_card_number(user_card[-16:])}"
        return mask_cart_numb

