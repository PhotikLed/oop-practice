"""Тема: Объекты и классы.

Задача: симуляция выращивания колонии бактерий в чашке Петри.
"""


class BacteriaProducer:
    """Управляет популяцией бактерий с контролем максимальной вместимости."""

    def __init__(self, max_bacteria: int) -> None:
        """Инициализирует лимит популяции и текущий счетчик."""
        self.max_bacteria = max_bacteria
        self.current_bacteria_count = 0

    def create(self) -> None:
        """Добавляет одну бактерию в колонию при наличии свободного места."""
        if self.current_bacteria_count >= self.max_bacteria:
            print('Нет места под новую бактерию')
        else:
            self.current_bacteria_count += 1
            print(
                f'Добавлена одна бактерия. '
                f'Бактерий в колонии: {self.current_bacteria_count}'
            )

    def delete(self) -> None:
        """Удаляет одну бактерию из популяции, если колония не пуста."""
        if self.current_bacteria_count <= 0:
            print('В популяции нет бактерий, удалять нечего')
        else:
            self.current_bacteria_count -= 1
            print(
                f'Одна бактерия удалена. '
                f'Бактерий в колонии: {self.current_bacteria_count}'
            )


if __name__ == '__main__':
    # Пример из описания задания
    bacteria_producer = BacteriaProducer(max_bacteria=3)
    bacteria_producer.delete()
    bacteria_producer.create()
    bacteria_producer.create()
    bacteria_producer.create()
    bacteria_producer.create()
    bacteria_producer.delete()
