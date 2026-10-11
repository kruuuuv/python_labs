"""Тесты для src/lib/text.py."""

import pytest

from src.lib.text import normalize, tokenize, count_freq, top_n

# ---------- normalize ----------


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("!!!", "!!!"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected

def test_normalize_casefold_false():
    """Ветка casefold=False использует .lower() вместо .casefold()."""
    # "ß".casefold() == "ss", "ß".lower() == "ß" — разница видна
    assert normalize("Straße", casefold=False) == "straße"
    assert normalize("Straße", casefold=True) == "strasse"

def test_normalize_yo2e_false():
    """Ветка yo2e=False не заменяет ё → е."""
    assert normalize("ёжик", yo2e=False) == "ёжик"
    assert normalize("ёжик", yo2e=True) == "ежик"


def test_normalize_whitespace_chars():
    """Все виды пробельных символов (\\t \\n \\r \\v \\f) заменяются на пробел."""
    assert normalize("a\tb\nc\rd\ve\ff") == "a b c d e f"


def test_normalize_multiple_spaces():
    """Несколько подряд идущих пробелов сжимаются в один."""
    assert normalize("a    b   c") == "a b c"


def test_normalize_strip():
    """Пробелы по краям убираются."""
    assert normalize("   abc   ") == "abc"

# ---------- tokenize ----------


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("Привет, мир!", ["Привет", "мир"]),
        ("test123 abc", ["test123", "abc"]),
        ("", []),
        ("!!! ... ???", []),
        ("один два три", ["один", "два", "три"]),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected

def test_tokenize_hyphen_word():
    """Слова с дефисом склеиваются: по-настоящему → одно слово."""
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]


def test_tokenize_trailing_hyphen():
    """Слово, заканчивающееся на дефис, отбрасывается."""
    assert tokenize("abc- def") == ["def"]


def test_tokenize_digits():
    """Цифры — часть слова: 2025 — токен."""
    assert tokenize("2025 год") == ["2025", "год"]


def test_tokenize_emoji():
    """Эмодзи — не часть слова, отбрасываются."""
    assert tokenize("emoji 😀 не слово") == ["emoji", "не", "слово"]


def test_tokenize_underscore():
    """Подчёркивание — часть слова: foo_bar — один токен."""
    assert tokenize("foo_bar baz") == ["foo_bar", "baz"]

# ---------- count_freq ----------


def test_count_freq_basic():
    tokens = ["a", "b", "a", "c", "a", "b"]
    assert count_freq(tokens) == {"a": 3, "b": 2, "c": 1}


def test_count_freq_empty():
    assert count_freq([]) == {}


def test_count_freq_all_same():
    assert count_freq(["x"] * 5) == {"x": 5}


# ---------- top_n ----------


def test_top_n_basic():
    freq = {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]


def test_top_n_more_than_items():
    freq = {"a": 1}
    assert top_n(freq, 10) == [("a", 1)]


def test_top_n_tie_breaker():
    """При равных частотах — сортировка по алфавиту."""
    freq = {"banana": 2, "apple": 2, "cherry": 2}
    assert top_n(freq, 3) == [("apple", 2), ("banana", 2), ("cherry", 2)]


def test_top_n_empty():
    assert top_n({}, 5) == []
