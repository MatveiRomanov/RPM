from typing import Generic, TypeVar

T = TypeVar('T')


class Point(Generic[T]):
    def __init__(self, x: T, y: T, z: T):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y}, {self.z})"