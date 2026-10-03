def normalize(s: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold == True:
        s = s.casefold()
    else: s = s.lower()
    if yo2e == True:
        s = s.replace("ё", "е").replace("Ё", "Е")

    for ch in "\t\n\r\v\f":
        s = s.replace(ch, " ")

    while "  " in s:
        s = s.replace("  ", " ")

    return s.strip()


def tokenize(text: str) -> list[str]:
    tokens = []
    word = ""
    for ch in text:
        if ch.isalnum() or ch == "_":
            word += ch
        elif ch == "-" and word != "":
            word += ch
        else:
            if word != "" and word[-1] != "-":
                tokens.append(word)
            word = ""
    if word != "" and word[-1] != "-":
        tokens.append(word)
    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] = freq[token] + 1
        else:
            freq[token] = 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = list(freq.items())
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            a_word, a_count = items[j]
            b_word, b_count = items[j + 1]
            if b_count > a_count or (b_count == a_count and b_word < a_word):
                items[j], items[j + 1] = items[j + 1], items[j]
    return items[:n]


print(normalize("ПрИвЕт\nМИр\t"))          # привет мир
print(normalize("ёжик, Ёлка"))             # ежик, елка
print(normalize("Hello\r\nWorld"))         # hello world
print(normalize("  двойные   пробелы  "))  # двойные пробелы

print(tokenize("привет мир"))              # ['привет', 'мир']
print(tokenize("hello,world!!!"))          # ['hello', 'world']
print(tokenize("по-настоящему круто"))     # ['по-настоящему', 'круто']
print(tokenize("2025 год"))                # ['2025', 'год']
print(tokenize("emoji 😀 не слово"))       # ['emoji', 'не', 'слово']

print(count_freq(["a","b","a","c","b","a"]))            # {'a': 3, 'b': 2, 'c': 1}
print(top_n({"a":3,"b":2,"c":1}, n=2))                  # [('a', 3), ('b', 2)]
print(top_n(count_freq(["bb","aa","bb","aa","cc"]), 2)) # [('aa', 2), ('bb', 2)]