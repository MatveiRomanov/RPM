from dataclasses import dataclass
from typing import List


@dataclass
class Book:
    title: str
    author: str
    year: int
    price: float


def sort_books_by_year(books: List[Book]) -> List[Book]:
    return sorted(books, key=lambda book: book.year)


def task1_demo():
    books = [
        Book("Война и мир", "Лев Толстой", 1869, 1200.0),
        Book("Преступление и наказание", "Фёдор Достоевский", 1866, 950.5),
        Book("Мастер и Маргарита", "Михаил Булгаков", 1967, 1100.0),
        Book("Евгений Онегин", "Александр Пушкин", 1833, 800.0)
    ]

    print("=== Задание 1: Книги ===")
    print("Исходный список:")
    for book in books:
        print(f"  {book.title} ({book.year}) - {book.price} руб.")

    sorted_books = sort_books_by_year(books)
    print("\nОтсортировано по году:")
    for book in sorted_books:
        print(f"  {book.title} ({book.year}) - {book.price} руб.")

    return books