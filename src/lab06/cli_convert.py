import argparse

import sys
from pathlib import Path

from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="CLI‑конвертеры лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда json2csv
    p1 = subparsers.add_parser("json2csv", help="JSON → CSV")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    # подкоманда csv2json
    p2 = subparsers.add_parser("csv2json", help="CSV → JSON")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    # подкоманда csv2xlsx
    p3 = subparsers.add_parser("csv2xlsx", help="CSV → XLSX")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    if args.command == "json2csv":
        json_to_csv(args.input, args.output)
        print(f"[OK] {args.input} → {args.output}")

    elif args.command == "csv2json":
        csv_to_json(args.input, args.output)
        print(f"[OK] {args.input} → {args.output}")

    elif args.command == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)
        print(f"[OK] {args.input} → {args.output}")

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()