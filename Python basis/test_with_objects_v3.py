import csv
import os

import pytest

from models.providers import UserProvider, CsvUserProvider, DatabaseUserProvider, ApiUserProvider
from models.users import User, USER_ADULT_AGE, Status, Worker

CURRENT_FILE_PATH = os.path.dirname(__file__)
PROJECT_ROOT_PATH = os.path.dirname(CURRENT_FILE_PATH)
TEMP_PATH = os.path.join(PROJECT_ROOT_PATH, 'temp')
csv_file_path = os.path.join(TEMP_PATH, 'users.csv')


@pytest.fixture(params=[CsvUserProvider, DatabaseUserProvider, ApiUserProvider])
def user_provider(request) -> UserProvider:
    return request.param()


"""@pytest.fixture
def user_provider() -> UserProvider:
    return CsvUserProvider()"""  # Эта фикстура возьмет данные только от csv,
    # а фикстура выше запустит 3 отдельных теста от 3-ех разных источников данных!


@pytest.fixture
def users(user_provider) -> list[User]:
    return user_provider.get_users()  # Таким образом в самом тесте не важно, откуда берем - csv, db, api,
    # мы вызываем общий get_users


@pytest.fixture
def workers(users) -> list[Worker]:
    # Берем только работников из списка пользователей
    workers = [Worker(name=user.name, age=user.age, items=user.items)
               for user in users if user.status == Status.worker]  # благодаря ссылке на класс Status,
    # лишаем себя возможности ошибиться в написании, а если кто-то ошибся в данных (в бд, в файле),
    # то мы сразу узнаем это, ведь такого статуса нет
    return workers


def user_id_adult(user):
    return user.age >= 18


def test_workers_are_adults_v3(workers):
    """
    Тестируем, что все работники старше 18 лет
    """

    for worker in workers:
        assert worker.is_adult(), f'Worker {worker.name} младше {USER_ADULT_AGE} лет'  # Проверка не пройдет без конвертации в int
        #assert not worker.is_adult() - ассерты лучше не реализовывать в классе,
        # а в самом тесте добавить not если нужна обратная ситуация,
        # потому как иначе понадобится писать 2 функции, зачем это