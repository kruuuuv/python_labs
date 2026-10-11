from pathlib import Path
import csv
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:

    """
    Открыть файл на чтение в указанной кодировке и вернуть содержимое как одну строку.
    Если файл не найден — FileNotFoundError.
    Если кодировка не подходит — UnicodeDecodeError.
    path: путь к файлу.
    encoding: кодировка файла (по умолчанию "utf-8")
        изменить кодировку: encoding="cp1251"
    """

    p = Path(path)
   
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:

    """
    Создать/перезаписать CSV с разделителем ','.
    header будет записан первой строкой.
    Проверка на одинаковую длину строк (иначе ValueError).
    """

    p = Path(path)
    rows = list(rows)

    if rows:
        row_length = len(rows[0])
        for row in rows:
            if len(row) != row_length:
                raise ValueError("Все строки должны иметь одинаковую длину.")
    
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

def ensure_parent_dir(path: str | Path) -> None:
    """Создать родительские директории, если их нет."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    
    from io_txt_csv import read_text, write_csv
    write_csv([("word", "count"), ("test", 3)], "data/result.csv")
    try:
        txt = read_text("data\lab04\input.txt")
        print("Файл успешно прочитан")
    except FileNotFoundError:
        print("Файл input.txt не найден")
    except UnicodeDecodeError:
        print("Ошибка кодировки при чтении файла")