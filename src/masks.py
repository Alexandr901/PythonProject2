def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты"""
    card_str = str(card_number)
    if len(card_str) != 16:
        raise ValueError
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

print(get_mask_card_number("7000792289606361"))

def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета"""
    acc_num = str(account_number)
    if len(acc_num) != 20:
        raise ValueError
    return f"**{account_number[-4:]}"
