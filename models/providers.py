import csv
import os
from models.users import User, Status


CURRENT_FILE_PATH = os.path.dirname(__file__)
PROJECT_ROOT_PATH = os.path.dirname(CURRENT_FILE_PATH)
TEMP_PATH = os.path.join(PROJECT_ROOT_PATH, 'temp')
csv_file_path = os.path.join(TEMP_PATH, 'users.csv')


# Это АБСТРАКТНЫЙ класс, обозначающий как мы будем брать наши данные,
# а классы далее - уже с конкретикой
class UserProvider:

    def get_users(self) -> list[User]:
        raise NotImplementedError  # При попытке вызвать данную функцию просто так, будет ошибка,
        # что эта функция не реализована. Потому что вызывать мы будем др. функции, других классов,
        # которые наследуют этот абстрактный класс (см. ниже)


class CsvUserProvider(UserProvider):
    # Пробегаемся по каждой строчке словарика и для каждой записи создаем собственный экземпляр класса
    def get_users(self) -> list[User]: # Это значит будет возвращать список
        with open(csv_file_path) as f:
            users = list(csv.DictReader(f, delimiter=';'))
        return [
            User(name=user['name'],
                 age=int(user['age']),
                 status=Status(user['status']),
                 items=user['items'])
            for user in users]


class DatabaseUserProvider(UserProvider):
    def get_users(self) -> list[User]:
        raise NotImplementedError


class ApiUserProvider(UserProvider):
    def get_users(self) -> list[User]:
        raise NotImplementedError
