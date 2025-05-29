from src.processing import filter_by_state, sort_by_date
from src.transaction_reader import read_csv, read_excel, search_transactions_by_description
from src.utils import load_transactions
from src.widget import get_date, mask_account_card


def main():
    """Общая функция по сборке всего проекта"""
    while True:
        print(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
            Выберите необходимый пункт меню:
                1. Получить информацию о транзакциях из JSON-файла
                2. Получить информацию о транзакциях из CSV-файла
                3. Получить информацию о транзакциях из XLSX-файла
            """
        )
        answer_1 = input("Введите число: ")

        if answer_1 == "1":
            print("Для обработки выбран JSON-файл")
            operations = load_transactions(r"C:\Users\A\PycharmProjects\PythonProject2\data\operations.json")
            break
        elif answer_1 == "2":
            print("Для обработки выбран CSV-файл")
            operations = read_csv(r"C:\Users\A\PycharmProjects\PythonProject2\data\transactions.csv")
            break
        elif answer_1 == "3":
            print("Для обработки выбран Excel-файл")
            operations = read_excel(
                r"C:\Users\A\PycharmProjects\PythonProject2\data\transactions_excel.xlsx"
            )
            break
        else:
            print("\nОшибка ввода! Такого пункта не существует.\nПопробуйте ещё раз.\n ")

    while True:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию.
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )
        answer_2 = input("Ваш ответ: ").upper()

        if answer_2 in {"EXECUTED", "CANCELED", "PENDING"}:
            filtered_operations = filter_by_state(operations, answer_2)
            print(f"Операции отфильтрованы по статусу {answer_2}")
            break
        else:
            print(f"Статус операции {answer_2} недоступен.\nПопробуйте снова.\n ")

    while True:
        print("Отсортировать операции по дате? Да/Нет")
        filter1 = input("Введите 'да' или 'нет': ").lower()

        if filter1 == "да":
            print("Отсортировать по возрастанию или по убыванию?")
            filter1_1 = input("по возрастанию/по убыванию: ").lower()
            if filter1_1 == "по убыванию":
                filtered_operations_dy_date = sort_by_date(filtered_operations, True)
                break
            elif filter1_1 == "по возрастанию":
                filtered_operations_dy_date = sort_by_date(filtered_operations, False)
                break
            else:
                print("\nОшибка ввода!\nПопробуйте ещё раз.\n ")
        elif filter1 == "нет":
            filtered_operations_dy_date = filtered_operations
            break
        else:
            print("\nОшибка ввода!\nПопробуйте ещё раз.\n ")

    filtered_operations_dy_currency = []

    while True:
        filter2 = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
        if filter2 in ["да", "нет"]:
            break

    if filter2 == "да":
        for operation in filtered_operations_dy_date:
            if "operationAmount" in operation and "currency" in operation["operationAmount"]:
                if operation["operationAmount"]["currency"]["code"] == "RUB":
                    filtered_operations_dy_currency.append(operation)

    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        filter3 = input("Введите 'да' или 'нет': ").lower()

        if filter3 == "да":
            user_search = input("Введите слово или фразу для поиска: ")
            filtered_operations_dy_descr = search_transactions_by_description(filtered_operations_dy_currency, user_search)
            break
        elif filter3 == "нет":
            filtered_operations_dy_descr = filtered_operations_dy_currency
            break
        else:
            print("Ошибка ввода! Попробуйте ещё раз.\n")

    if len(filtered_operations_dy_descr) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return []

    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(filtered_operations_dy_descr)}\n")

    for operation in filtered_operations_dy_descr:
        date = get_date(operation.get("date"))
        description = operation.get("description")
        print(f"{date} {description}")

        if operation.get("description") == "Открытие вклада":
            acc_number = mask_account_card(operation["to"])
            print(acc_number)
            if answer_1 == "1":
                amount = operation["operationAmount"]["amount"]
                currency_name = operation["operationAmount"]["currency"]["name"]
                print(f"Сумма: {amount} {currency_name}")
            elif answer_1 == "2" or answer_1 == "3":
                amount = operation["amount"]
                currency_name = operation["currency_name"]
                print(f"Сумма: {amount} {currency_name}")
        else:
            acc_number_from = mask_account_card(operation["from"])
            acc_number_to = mask_account_card(operation["to"])
            print(f"{acc_number_from} -> {acc_number_to}")
            if answer_1 == "1":
                amount = operation["operationAmount"]["amount"]
                currency_name = operation["operationAmount"]["currency"]["name"]
                print(f"Сумма: {amount} {currency_name}")
            elif answer_1 == "2" or answer_1 == "3":
                amount = operation["amount"]
                currency_name = operation["currency_name"]
                print(f"Сумма: {amount} {currency_name}")


if __name__ == "__main__":
    result = main()
