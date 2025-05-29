import re
from collections import Counter

import pandas as pd


def read_csv(file_path):
    """Функция для считывания финансовых операций из CSV"""
    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")


def read_excel(file_path):
    """Функция для считывания финансовых операций из EXCEL"""
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")


def search_transactions_by_description(transactions, search_string):
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка.
    """
    result = []
    for transaction in transactions:
        if re.search(search_string, transaction.get("description", ""), re.I):
            result.append(transaction)
    return result


def count_transactions_by_category(transactions, categories):
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь.
    """
    category_counts = Counter()
    for transaction in transactions:
        for category in categories:
            if category.lower() in transaction.get("description", "").lower():
                category_counts[category] += 1
    return dict(category_counts)
