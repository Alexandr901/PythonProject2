import logging
import os.path

if not os.path.exists("logs"):
    os.makedirs("logs")

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты"""
    card_str = str(card_number)
    if len(card_str) != 16:
        logging.error("Неккоректная длина номера карты")
        raise ValueError
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета"""
    acc_num = str(account_number)
    if len(acc_num) < 4:
        logging.error("Неккоректная длина номера карты")
        raise ValueError
    return f"**{account_number[-4:]}"
