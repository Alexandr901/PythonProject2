import pandas as pd


def read_csv(file_path):
    """Функция для считывания финансовых операций из CSV"""
    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")


def read_excel(file_path):
    """Функция для считывания финансовых операций из EXCEL"""
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")
