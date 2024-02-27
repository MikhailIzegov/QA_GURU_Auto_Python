import csv
import os

CURRENT_FILE_PATH = os.path.dirname(__file__)
PROJECT_ROOT_PATH = os.path.dirname(CURRENT_FILE_PATH)
TEMP_PATH = os.path.join(PROJECT_ROOT_PATH, 'temp')


def test_workers_are_adults():
    """
    Тестируем, что все работники старше 18 лет
    """
    csv_file_path = os.path.join(TEMP_PATH, 'users_for_tests.csv')
    print(csv_file_path)
    with open(csv_file_path) as f:
        users = csv.DictReader(f, delimiter=';')
        # В одну строку:
        workers = [user for user in users if user['status'] == 'worker']

        # В много строк:
        """
        workers = []
        for user in users_for_tests:
            if user['status'] == 'worker':
                workers.append(user)
                """
        # То же самое можно делать со словарями: {key: value for key, value in some_dict.items() if ...}

    for worker in workers:
        assert int(worker['age']) >= 18  # Проверка не пройдет без конвертации в int
