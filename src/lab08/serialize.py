import json
from pathlib import Path

from src.lab08.models import Student


def students_to_json(students: list[Student], path: str | Path) -> None:
    """Сохранить список студентов в JSON."""
    data = [s.to_dict() for s in students]

    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    with p.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str | Path) -> list[Student]:
    """Прочитать JSON и вернуть список Student.

    FileNotFoundError — если файла нет.
    ValueError — если структура не список словарей.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Файл не найден: {p}")

    with p.open(encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("JSON должен быть массивом объектов")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Каждый элемент JSON должен быть словарём")

    return [Student.from_dict(item) for item in data]