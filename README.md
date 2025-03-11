# Bank Project

Данный проект представляет собой виджет (или модуль) для работы с банковскими операциями клиентов.
Цель — фильтрация и сортировка списка банковских операций.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Alexandr901/PythonProject2.git
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd PythonProject2
   ```
3. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Использование

Примеры использования функций:

```python

from src.processing import filter_by_state

operations_data = [
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
]

# Получаем операции со статусом EXECUTED
executed_ops = filter_by_state(operations_data)
print(executed_ops)

# Сортируем по дате (по убыванию)
sorted_ops_desc = sort_by_date(operations_data)
print(sorted_ops_desc)
```

### Тестирование

Для тестирования проекта используется библиотека `pytest`. 
Чтобы запустить тесты, выполните команду:

```bash
  pytest
```

Тесты покрывают следующие модули и функции:
- `masks`: функции `get_mask_card_number` и `get_mask_account`.
- `widget`: функции `get_account_card` и `get_data`.
- `processing`: функции `filter_by_state` и `sort_by_date`.
- `generators`: функции и генераторы `filter_by_currency`, `transaction_descriptions` и `card_number_generator`.
- `decorators`: декоратор `log`

- Покрытие тестами составляет более 80% кода проекта.