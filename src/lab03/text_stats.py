import os
import sys

from lib.text import normalize, tokenize, count_freq, top_n

TABLE_MODE = os.environ.get("TABLE_MODE", "0") == "1"


def print_top5(top: list[tuple[str, int]]) -> None:
    """Печатает топ-5 в обычном режиме: слово:кол-во построчно."""
    print("Топ-5:")
    for word, count in top:
        print(f"{word}:{count}")


def print_top5_table(top: list[tuple[str, int]]) -> None:
    """Печатает топ-5 в виде выровненной таблицы."""
    if not top:
        print("Топ-5: (пусто)")
        return

    width = 0
    for word, _ in top:
        if len(word) > width:
            width = len(word)

    # Заголовок
    header_word = "слово"
    if len(header_word) > width:
        width = len(header_word)

    print(f"{header_word:<{width}} | частота")
    print("-" * (width + 1 + 1 + 7))  # word + " | " + "частота"
    for word, count in top:
        print(f"{word:<{width}} | {count}")


def main() -> None:
    # читаем весь stdin до EOF
    text = sys.stdin.read()

    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top = top_n(freq, n=5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")

    if TABLE_MODE:
        print_top5_table(top)
    else:
        print_top5(top)


if __name__ == "__main__":
    main()
