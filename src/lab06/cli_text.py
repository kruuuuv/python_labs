import argparse

import re
import sys
from collections import Counter
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        try:
            lines = Path(args.input).read_text(encoding="utf-8").splitlines()
        except FileNotFoundError:
            print(f"Ошибка: файл не найден: {args.input}", file=sys.stderr)
            sys.exit(1)

        for i, line in enumerate(lines, start=1):
            if args.n:
                print(f"{i:>6}\t{line}")
            else:
                print(line)

    elif args.command == "stats":
        try:
            text = Path(args.input).read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"Ошибка: файл не найден: {args.input}", file=sys.stderr)
            sys.exit(1)

        words = re.findall(r"\w+", text.lower(), flags=re.UNICODE)
        freq = Counter(words)

        print(f"Всего слов: {len(words)}")
        print(f"Уникальных: {len(freq)}")
        print(f"Топ-{args.top}:")
        for word, count in freq.most_common(args.top):
            print(f"  {word}: {count}")

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
