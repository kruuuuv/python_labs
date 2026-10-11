from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class Student:
    """Студент: ФИО, дата рождения, группа, средний балл."""

    fio: str
    birthdate: str  # формат YYYY-MM-DD
    group: str
    gpa: float

    def __post_init__(self) -> None:
        """Валидация: формат даты и диапазон gpa."""
        # 1) формат даты
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(
                f"birthdate должен быть в формате YYYY-MM-DD, получено: {self.birthdate!r}"
            ) from e

        # 2) диапазон gpa
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"gpa должен быть в диапазоне 0..5, получено: {self.gpa}")

    def age(self) -> int:
        """Количество полных лет."""
        b = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        years = today.year - b.year
        # если день рождения в этом году ещё не наступил — минус год
        if (today.month, today.day) < (b.month, b.day):
            years -= 1
        return years

    def to_dict(self) -> dict:
        """Сериализация в словарь."""
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Student":
        """Десериализация из словаря."""
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=d["gpa"],
        )

    def __str__(self) -> str:
        """Красивый вывод."""
        return f"{self.fio} ({self.group}), {self.age()} лет, GPA={self.gpa}"