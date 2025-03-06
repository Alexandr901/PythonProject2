from datetime import datetime
from typing import Any


def filter_by_state(operations: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Возвращает новый список словарей по указанному значению"""
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: list[dict[str, Any]], descending: bool = True) -> list[dict[str, Any]]:
    """Возвращает новый список отсортированный по дате"""
    sorted_operations = sorted(operations, key=lambda op: datetime.fromisoformat(op["date"]), reverse=descending)
    return sorted_operations
