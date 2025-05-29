import json
import logging
import os

if not os.path.exists("logs"):
    os.makedirs("logs")

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def load_transactions(file_path):
    """Загрузить транзакции из JSON-файла."""
    if not os.path.isfile(file_path):
        logger.error(f"Файл {file_path} не найден")
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Транзакции успешно загружены")
                return data
            else:
                logger.warning("Данные не являются списком")
                return []
        except json.JSONDecodeError as e:
            logger.error(f"Ошибка при загрузке JSON: {e}")
            return []
