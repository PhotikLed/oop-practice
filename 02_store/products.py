"""Тема: Знакомство с ООП и наследованием.

Задача: учет товаров в торговой сети с полиморфными методами получения информации.
"""

from typing import Union


class Product:
    """Базовый класс товара."""

    def __init__(self, name: str, quantity: int) -> None:
        """Инициализация общих атрибутов товара."""
        self.name = name
        self.quantity = quantity

    def get_basic_info(self) -> str:
        """Возвращает строку с названием товара и остатком на складе."""
        return f'{self.name} (в наличии: {self.quantity})'

    def get_full_info(self) -> str:
        """Возвращает полное описание товара. Переопределяется в наследниках."""
        pass


class Kettlebell(Product):
    """Спортивный товар: гиря с указанием веса."""

    def __init__(
        self,
        name: str,
        quantity: int,
        weight: Union[int, float]
    ) -> None:
        """Вызывает конструктор базового класса и сохраняет вес гири."""
        super().__init__(name, quantity)
        self.weight = weight

    def get_full_info(self) -> str:
        """Формирует строку: базовое описание + вес в килограммах."""
        return f'{self.get_basic_info()}. Вес: {self.weight} кг'


class Clothing(Product):
    """Предмет одежды с указанием размера."""

    def __init__(self, name: str, quantity: int, size: str) -> None:
        """Вызывает конструктор базового класса и сохраняет размер."""
        super().__init__(name, quantity)
        self.size = size

    def get_full_info(self) -> str:
        """Формирует строку: базовое описание + размер одежды."""
        return f'{self.get_basic_info()}. Размер: {self.size}'


if __name__ == '__main__':
    small_kettlebell = Kettlebell('Гиря малая', 15, 2)
    shirt = Clothing('Футболка', 5, 'L')

    print(small_kettlebell.get_full_info())
    print(shirt.get_full_info())
