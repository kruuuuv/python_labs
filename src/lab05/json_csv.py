"""JSON ↔ CSV: двусторонняя конвертация списка словарей."""

import csv
import json
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """JSON-список словарей → CSV.

    Отсутствующие поля заполняются пустыми строками.
    Колонки — в порядке первого объекта.
    """
    p = Path(json_path)
    if not p.exists():
        raise FileNotFoundError(f"Файл не найден: {json_path}")

    with p.open(encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list) or not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON должен быть списком словарей")

    fieldnames = list(data[0].keys())

    out = Path(csv_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in data:
            w.writerow({k: row.get(k, "") for k in fieldnames})


def csv_to_json(csv_path: str, json_path: str) -> None:
    """CSV с заголовком → JSON-список словарей (значения — строки)."""
    p = Path(csv_path)
    if not p.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    with p.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV без заголовка")
        rows = list(reader)

    if not rows:
        raise ValueError("Пустой CSV")

    out = Path(json_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
