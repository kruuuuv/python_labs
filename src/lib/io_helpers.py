import sys
from pathlib import Path


def read_lines(path: str | Path) -> list[str]:
    """Прочитать файл как список строк без \\n."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Файл не найден: {p}")
    return p.read_text(encoding="utf-8").splitlines()


def print_error(msg: str) -> None:
    """Напечатать сообщение об ошибке в stderr."""
    print(f"Ошибка: {msg}", file=sys.stderr)
