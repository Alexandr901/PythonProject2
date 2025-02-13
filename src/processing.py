from typing import Any


def filter_by_state(operations: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Возвращает новый список словарей по указанному значению"""
    return [op for op in operations if op.get("state") == state]
