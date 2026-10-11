
import sys
from pathlib import Path


import argparse
from collections import Counter

from src.lab04.io_txt_csv import read_text, write_csv, ensure_parent_dir
from src.lib.text import normalize, tokenize, count_freq, top_n


def collect_frequencies(input_paths: list[str], encoding: str = "utf-8") -> Counter:
    """Прочитать все файлы, вернуть суммарные частоты слов."""
    total: Counter = Counter()
    for path in input_paths:
        try:
            text = read_text(path, encoding)
        except FileNotFoundError:
            print(f"Ошибка: файл {path} не найден.")
            sys.exit(1)
        except UnicodeDecodeError:
            print(f"Ошибка: файл {path} — укажите другую кодировку (--encoding).")
            sys.exit(1)

        tokens = tokenize(normalize(text))
        total.update(count_freq(tokens))
    return total


def create_report(input_paths: list[str], output_path: str,
                  encoding: str = "utf-8") -> None:
    """Считать частоты из одного/нескольких файлов и записать CSV.

    В консоль печатает: число файлов, всего слов, уникальных, топ-5.
    """
    freq = collect_frequencies(input_paths, encoding)

    total_words = sum(freq.values())
    unique_words = len(freq)
    top5 = top_n(freq, 5)

    rows = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

    ensure_parent_dir(output_path)
    write_csv(rows, output_path, header=("word", "count"))

    print(f"Файлов обработано: {len(input_paths)}")
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top5:
        print(f"  {word}: {count}")
    print(f"Записано: {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Отчёт о частоте слов из текстовых файлов."
    )
    parser.add_argument(
        "--in", dest="input_files", nargs="+",
        default=["data/lab04/input.txt","data/lab04/a.txt","data/lab04/b.txt"],
        help="Один или несколько входных .txt файлов."
    )
    parser.add_argument(
        "--out", dest="output_file",
        default="data/lab04/report.csv",
        help="Путь к выходному CSV.",
    )
    parser.add_argument("--encoding", default="utf-8")
    args = parser.parse_args()

    create_report(args.input_files, args.output_file, args.encoding)


if __name__ == "__main__":
    main()