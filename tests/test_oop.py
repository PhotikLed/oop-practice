"""Юнит-тесты для заданий по объектно-ориентированному программированию."""

from importlib import import_module

bacteria_mod = import_module('01_bacteria.bacteria')
store_mod = import_module('02_store.products')
validator_mod = import_module('03_exceptions.date_validator')
gen_mod = import_module('04_advanced.generators')


def test_bacteria_producer(capsys):
    """Проверяет жизненный цикл колонии бактерий и граничные случаи."""
    producer = bacteria_mod.BacteriaProducer(max_bacteria=2)
    assert producer.current_bacteria_count == 0

    # Попытка удалить из пустой чашки
    producer.delete()
    assert 'В популяции нет бактерий, удалять нечего' in capsys.readouterr().out
    assert producer.current_bacteria_count == 0

    # Добавление бактерий
    producer.create()
    assert producer.current_bacteria_count == 1
    assert 'Добавлена одна бактерия. Бактерий в колонии: 1' in capsys.readouterr().out

    producer.create()
    assert producer.current_bacteria_count == 2

    # Превышение лимита
    producer.create()
    assert 'Нет места под новую бактерию' in capsys.readouterr().out
    assert producer.current_bacteria_count == 2

    # Удаление
    producer.delete()
    assert producer.current_bacteria_count == 1
    assert 'Одна бактерия удалена. Бактерий в колонии: 1' in capsys.readouterr().out


def test_store_inheritance():
    """Проверяет наследование и полиморфизм классов Product, Kettlebell и Clothing."""
    kettlebell = store_mod.Kettlebell('Гиря малая', 15, 2)
    clothing = store_mod.Clothing('Футболка', 5, 'L')

    assert kettlebell.get_basic_info() == 'Гиря малая (в наличии: 15)'
    assert kettlebell.get_full_info() == 'Гиря малая (в наличии: 15). Вес: 2 кг'

    assert clothing.get_basic_info() == 'Футболка (в наличии: 5)'
    assert clothing.get_full_info() == 'Футболка (в наличии: 5). Размер: L'

    assert isinstance(kettlebell, store_mod.Product)
    assert isinstance(clothing, store_mod.Product)


def test_date_validator(capsys):
    """Проверяет валидацию дат и подсчет статистики записей."""
    assert validator_mod.validate_record('Иван', '16.09.1990') is True

    assert validator_mod.validate_record('Петр', '23 марта 1791 года') is False
    expected_msg = 'Некорректный формат даты в записи: Петр, 23 марта 1791 года'
    assert expected_msg in capsys.readouterr().out

    entries = [
        ('Акакій Башмачкинъ', '23 марта 1791 года'),
        ('Яков Степанов', 'Двадцать шестое июля 1971'),
        ('Потап Алексеев', '16.09.1990'),
        ('Евгений Женин', '5 декабря 1984'),
        ('Кондрат Александров', '18.01.1994')
    ]
    stats = validator_mod.process_people(entries)
    assert stats == {'good': 2, 'bad': 3}


def test_fibonacci():
    """Проверяет генератор чисел Фибоначчи."""
    assert list(gen_mod.fibonacci(0)) == []
    assert list(gen_mod.fibonacci(1)) == [0]
    assert list(gen_mod.fibonacci(2)) == [0, 1]
    assert list(gen_mod.fibonacci(6)) == [0, 1, 1, 2, 3, 5]
    assert list(gen_mod.fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
