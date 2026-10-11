"""Тесты для src/lab05/json_csv.py."""

import csv
import json
from pathlib import Path

import pytest

from src.lab05.json_csv import json_to_csv, csv_to_json

# ---------- позитивные сценарии ----------


def test_json_to_csv_basic(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())
    assert rows[0]["name"] == "Alice"
    assert rows[1]["name"] == "Bob"


def test_json_to_csv_missing_field(tmp_path: Path):
    """Отсутствующие поля заполняются пустыми строками."""
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22, "city": "SPB"},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    assert rows[1]["city"] == ""


def test_csv_to_json_basic(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    src.write_text(
        "name,age,city\nAlice,22,SPB\nBob,25,Moscow\n",
        encoding="utf-8",
    )

    csv_to_json(str(src), str(dst))

    data = json.loads(dst.read_text(encoding="utf-8"))
    assert len(data) == 2
    assert set(data[0].keys()) == {"name", "age", "city"}
    assert data[0]["name"] == "Alice"
    assert data[1]["age"] == "25"  # значения как строки


def test_json_csv_roundtrip(tmp_path: Path):
    """JSON → CSV → JSON: количество записей и набор ключей совпадают."""
    original = [
        {"name": "Alice", "age": "22", "city": "SPB"},
        {"name": "Bob", "age": "25", "city": "Moscow"},
    ]
    j1 = tmp_path / "people.json"
    c = tmp_path / "people.csv"
    j2 = tmp_path / "people2.json"

    j1.write_text(json.dumps(original, ensure_ascii=False), encoding="utf-8")

    json_to_csv(str(j1), str(c))
    csv_to_json(str(c), str(j2))

    result = json.loads(j2.read_text(encoding="utf-8"))
    assert len(result) == len(original)
    assert set(result[0].keys()) == set(original[0].keys())


# ---------- негативные сценарии ----------


def test_json_to_csv_empty_json(tmp_path: Path):
    src = tmp_path / "empty.json"
    dst = tmp_path / "out.csv"
    src.write_text("[]", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_not_a_list(tmp_path: Path):
    src = tmp_path / "obj.json"
    dst = tmp_path / "out.csv"
    src.write_text('{"name": "Alice"}', encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_list_not_of_dicts(tmp_path: Path):
    src = tmp_path / "list.json"
    dst = tmp_path / "out.csv"
    src.write_text("[1, 2, 3]", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_file_not_found(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        json_to_csv(str(tmp_path / "nope.json"), str(tmp_path / "out.csv"))


def test_csv_to_json_empty_csv(tmp_path: Path):
    src = tmp_path / "empty.csv"
    dst = tmp_path / "out.json"
    src.write_text("name,age\n", encoding="utf-8")  # только заголовок

    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst))


def test_csv_to_json_file_not_found(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        csv_to_json(str(tmp_path / "nope.csv"), str(tmp_path / "out.json"))

def test_csv_to_json_no_header(tmp_path: Path):
    """Совсем пустой CSV (0 байт) → ValueError."""
    src = tmp_path / "empty.csv"
    dst = tmp_path / "out.json"
    src.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst))