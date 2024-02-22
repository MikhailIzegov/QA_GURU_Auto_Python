import csv
import os

import pytest

CURRENT_FILE_PATH = os.path.dirname(__file__)
PROJECT_ROOT_PATH = os.path.dirname(CURRENT_FILE_PATH)
TEMP_PATH = os.path.join(PROJECT_ROOT_PATH, 'temp')
csv_file_path = os.path.join(TEMP_PATH, 'users.csv')


@pytest.fixture
def users():
    with open(csv_file_path) as f:
        users = list(csv.DictReader(f, delimiter=';'))
    return users


@pytest.fixture
def workers(users):
    # Берем только работников из списка пользователей
    workers = [user for user in users if user['status'] == 'worker']
    return workers


def user_id_adult(user):
    return int(user['age']) >= 18


def test_workers_are_adults_v3(workers):
    """
    Тестируем, что все работники старше 18 лет
    """

    for worker in workers:
        assert user_id_adult(worker)  # Проверка не пройдет без конвертации в int
