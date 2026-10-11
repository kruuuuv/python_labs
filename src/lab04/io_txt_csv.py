from pathlib import Path
import csv
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Прочитать файл целиком как одну строку.

    FileNotFoundError и UnicodeDecodeError не подавляются.
    Если кодировка не utf-8 — укажите явно, например: read_text("f.txt", encoding="cp1251").
    """
    return Path(path).read_text(encoding=encoding)


def write_csv(
    rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    """Записать CSV с разделителем ','.

    Если передан header — пишется первой строкой.
    Все строки должны быть одинаковой длины, иначе ValueError.
    """
    rows = list(rows)

    if rows:
        n = len(rows[0])
        for r in rows:
            if len(r) != n:
                raise ValueError("Все строки должны иметь одинаковую длину.")

    p = Path(path)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


def ensure_parent_dir(path: str | Path) -> None:
    """Создать родительские директории, если их нет."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
