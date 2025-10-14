from typing import Generic, TypeVar, List, Tuple

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')


class TaskManager(Generic[T, U, V]):
    def __init__(self):
        self.tasks: List[Tuple[T, U, V]] = []

    def add_task(self, id: T, description: U, priority: V) -> None:
        self.tasks.append((id, description, priority))

    def get_highest_priority_task(self) -> Tuple[T, U, V]:
        if not self.tasks:
            raise ValueError("No tasks available")

        # Определяем способ сравнения приоритетов
        if all(isinstance(task[2], (int, float)) for task in self.tasks):
            # Для числовых приоритетов ищем максимальное значение
            return max(self.tasks, key=lambda task: task[2])
        elif all(isinstance(task[2], bool) for task in self.tasks):
            # Для булевых приоритетов True считается выше
            for task in self.tasks:
                if task[2]:  # Если нашли задачу с True
                    return task
            return self.tasks[0]  # Если все False, возвращаем первую
        else:
            # Для других типов используем стандартное сравнение
            return max(self.tasks, key=lambda task: task[2])

    def __str__(self) -> str:
        if not self.tasks:
            return "No tasks"

        result = "Tasks:\n"
        for task in self.tasks:
            result += f"  ID: {task[0]}, Description: {task[1]}, Priority: {task[2]}\n"
        return result