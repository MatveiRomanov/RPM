from typing import Generic, TypeVar, List

T = TypeVar('T')


class TypedArray(Generic[T]):
    def __init__(self):
        self._items: List[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def get(self, index: int) -> T:
        if 0 <= index < len(self._items):
            return self._items[index]
        else:
            raise IndexError(f"Index {index} out of range for array of size {len(self._items)}")

    def __str__(self) -> str:
        return f"TypedArray{self._items}"