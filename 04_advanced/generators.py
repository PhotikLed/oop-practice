"""Тема: Расширенные возможности Python: генераторы и итераторы.

Задача: генератор чисел Фибоначчи.
"""

from typing import Iterator


def fibonacci(n: int) -> Iterator[int]:
    """Генератор n первых чисел последовательности Фибоначчи."""
    if n <= 0:
        return

    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


if __name__ == '__main__':
    sequence = fibonacci(10)
    for number in sequence:
        print(number)
