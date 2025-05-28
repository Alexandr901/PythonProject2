import pandas as pd

"""Функция для считывания финансовых операций из CSV"""
def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')


"""Функция для считывания финансовых операций из EXCEL"""
def read_excel(file_path):
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')
