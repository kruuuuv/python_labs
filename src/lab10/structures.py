from collections import deque
from typing import Any


class Stack:
    """Стек (LIFO) на базе list."""

    def __init__(self) -> None:
        self._data: list[Any] = []

    def push(self, item: Any) -> None:
        """Добавить элемент на вершину."""
        self._data.append(item)

    def pop(self) -> Any:
        """Снять верхний элемент. IndexError, если стек пуст."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Any | None:
        """Верхний элемент без удаления. None, если пусто."""
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        """True, если стек пуст."""
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Stack({self._data})"


class Queue:
    """Очередь (FIFO) на базе collections.deque."""

    def __init__(self) -> None:
        self._data: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        """Добавить элемент в конец очереди."""
        self._data.append(item)

    def dequeue(self) -> Any:
        """Взять элемент из начала. IndexError, если пусто."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self) -> Any | None:
        """Первый элемент без удаления. None, если пусто."""
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        """True, если очередь пуста."""
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Queue({list(self._data)})"