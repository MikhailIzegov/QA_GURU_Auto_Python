"""
Используем декоратор @dataclass, чтобы вручную не прописывать функции типа:
__функция__
Один раз прописали у класса декоратор - и все, под капотом они уже заложены.
Используется для работы с данными + объекты в дебаге будут легкочитаемы
"""
from dataclasses import dataclass


@dataclass  # Это называется модель - абстракция над какими-то данными
class User:
    name: str
    age: int
    status: str
    items: list[str]

    # def __init__(self, name, age, status, items):
    #     self.name = name
    #     self.age = age
    #     self.status = status
    #     self.items = items

    """
    Эта функция вызывается при сравнении двух объектов класса.
    Мы можем прописать внутри нее условия, соблюдая которые объекты будут равны друг другу
    Параметр self здесь это принадлежность к нашему классу User (oleg), 
    а Other это класс, с которым мы сравниваем (oleg2)
    """
    # def __eq__(self, other):
    #     return (self.name == other.name and
    #             self.age == other.age and
    #             self.status == other.status and
    #             self.items == other.items)


"""
Код в блоке if __name__ == '__main__': 
выполнится только при запуске скрипта напрямую, но не при его импорте как модуля.
"""
if __name__ == '__main__':
    # То же самое, что и Олег из csv
    d = {'name': 'Oleg',
         'age': 16,
         'status': 'student',
         'items': ['book', 'pen', 'paper']}

    oleg = User(name='Oleg', age=16, status='student', items=['book', 'pen', 'paper'])
    oleg2 = User(name='Oleg', age=16, status='student', items=['book', 'pen', 'paper'])
    olga = User(name='Olga', age=18, status='worker', items=['book', 'paper'])

    assert oleg == oleg2
