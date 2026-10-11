from __future__ import annotations

import csv
from pathlib import Path

from src.lab08.models import Student


class Group:
    """Хранилище студентов в CSV-файле с CRUD-операциями."""

    HEADER = ("fio", "birthdate", "group", "gpa")

    def __init__(self, storage_path: str | Path) -> None:
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    # ---------- внутренние методы ----------

    def _ensure_storage_exists(self) -> None:
        """Создать файл с заголовком, если его ещё нет."""
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            with self.path.open("w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(self.HEADER)

    def _read_all(self) -> list[dict]:
        """Прочитать все строки CSV. Проверить заголовок."""
        with self.path.open(encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None:
                raise ValueError("CSV пуст — нет заголовка")
            if tuple(reader.fieldnames) != self.HEADER:
                raise ValueError(
                    f"Неверный заголовок CSV. Ожидалось {self.HEADER}, "
                    f"получено {tuple(reader.fieldnames)}"
                )
            return list(reader)

    def _write_all(self, rows: list[dict]) -> None:
        """Перезаписать CSV переданными строками."""
        with self.path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=self.HEADER)
            w.writeheader()
            for r in rows:
                w.writerow({k: r[k] for k in self.HEADER})

    # ---------- CRUD ----------

    def list(self) -> list[Student]:
        """Все студенты как список Student."""
        rows = self._read_all()
        return [Student.from_dict({**r, "gpa": float(r["gpa"])}) for r in rows]

    def add(self, student: Student) -> None:
        """Добавить студента в CSV."""
        rows = self._read_all()
        rows.append({
            "fio": student.fio,
            "birthdate": student.birthdate,
            "group": student.group,
            "gpa": str(student.gpa),
        })
        self._write_all(rows)

    def find(self, substr: str) -> list[Student]:
        """Найти студентов по подстроке в ФИО."""
        rows = self._read_all()
        return [
            Student.from_dict({**r, "gpa": float(r["gpa"])})
            for r in rows
            if substr.lower() in r["fio"].lower()
        ]

    def remove(self, fio: str) -> int:
        """Удалить всех с указанным ФИО. Вернуть количество удалённых."""
        rows = self._read_all()
        new_rows = [r for r in rows if r["fio"] != fio]
        removed = len(rows) - len(new_rows)
        if removed:
            self._write_all(new_rows)
        return removed

    def update(self, fio: str, **fields) -> int:
        """Обновить поля студента(ов) с указанным ФИО. Вернуть количество обновлённых."""
        allowed = set(self.HEADER) - {"fio"}
        unknown = set(fields) - allowed
        if unknown:
            raise ValueError(f"Недопустимые поля для обновления: {unknown}")

        rows = self._read_all()
        count = 0
        for r in rows:
            if r["fio"] == fio:
                for k, v in fields.items():
                    r[k] = str(v)
                count += 1

        if count:
            # перепроверка: собрать Student'ов, чтобы валидация сработала
            for r in rows:
                Student.from_dict({**r, "gpa": float(r["gpa"])})
            self._write_all(rows)
        return count

    # ---------- ★ аналитика ----------

    def stats(self) -> dict:
        """Статистика по группе."""
        students = self.list()

        if not students:
            return {
                "count": 0,
                "min_gpa": None,
                "max_gpa": None,
                "avg_gpa": None,
                "groups": {},
                "top_5_students": [],
            }

        gpas = [s.gpa for s in students]

        groups: dict[str, int] = {}
        for s in students:
            groups[s.group] = groups.get(s.group, 0) + 1

        top5 = sorted(students, key=lambda s: -s.gpa)[:5]

        return {
            "count": len(students),
            "min_gpa": min(gpas),
            "max_gpa": max(gpas),
            "avg_gpa": round(sum(gpas) / len(gpas), 2),
            "groups": groups,
            "top_5_students": [{"fio": s.fio, "gpa": s.gpa} for s in top5],
        }