from typing import Any, Iterator


class Node:
    """Узел односвязного списка."""

    def __init__(self, value: Any, next: "Node | None" = None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.value!r})"


class SinglyLinkedList:
    """Односвязный список."""

    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None   # для O(1) append
        self._size: int = 0

    # ---------- вставка ----------

    def append(self, value: Any) -> None:
        """Добавить в конец. O(1) благодаря tail."""
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            assert self.tail is not None
            self.tail.next = node
            self.tail = node
        self._size += 1

    def prepend(self, value: Any) -> None:
        """Добавить в начало. O(1)."""
        node = Node(value, next=self.head)
        self.head = node
        if self.tail is None:
            self.tail = node
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        """Вставить по индексу idx (0..len). Иначе IndexError."""
        if idx < 0 or idx > self._size:
            raise IndexError(f"index out of range: {idx}")

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:
            self.append(value)
            return

        current = self.head
        for _ in range(idx - 1):
            assert current is not None
            current = current.next

        assert current is not None
        current.next = Node(value, next=current.next)
        self._size += 1

    # ---------- удаление ----------

    def remove(self, value: Any) -> bool:
        """Удалить первое вхождение value. True, если удалили."""
        prev: Node | None = None
        current = self.head

        while current is not None:
            if current.value == value:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                if current is self.tail:
                    self.tail = prev
                self._size -= 1
                return True
            prev = current
            current = current.next

        return False

    def remove_at(self, idx: int) -> Any:
        """Удалить элемент по индексу. Вернуть значение."""
        if idx < 0 or idx >= self._size:
            raise IndexError(f"index out of range: {idx}")

        prev: Node | None = None
        current = self.head
        for _ in range(idx):
            prev = current
            assert current is not None
            current = current.next

        assert current is not None
        value = current.value

        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next

        if current is self.tail:
            self.tail = prev

        self._size -= 1
        return value

    # ---------- протоколы ----------

    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"SinglyLinkedList({list(self)})"

    # ---------- ★ «красивый» вывод ----------

    def pretty(self) -> str:
        """Текстовое представление: [A] -> [B] -> None."""
        parts = [f"[{v}]" for v in self]
        parts.append("None")
        return " -> ".join(parts)