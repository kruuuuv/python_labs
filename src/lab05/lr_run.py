"""Демонстрация ЛР5: JSON→CSV, CSV→JSON, CSV→XLSX."""

from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main():
    # 1. JSON → CSV
    json_to_csv("data/lab05/samples/people.json", "data/lab05/out/people_from_json.csv")
    print("[OK] JSON → CSV: data/lab05/out/people_from_json.csv")

    # 2. CSV → JSON
    csv_to_json("data/lab05/samples/people.csv", "data/lab05/out/people_from_csv.json")
    print("[OK] CSV → JSON: data/lab05/out/people_from_csv.json")

    # 3. CSV → XLSX
    csv_to_xlsx("data/lab05/samples/cities.csv", "data/lab05/out/cities.xlsx")
    print("[OK] CSV → XLSX: data/lab05/out/cities.xlsx")


if __name__ == "__main__":
    main()
