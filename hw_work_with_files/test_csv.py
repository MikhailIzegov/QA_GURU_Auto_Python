import csv
import os

from hw_work_with_files.conftest import TEMP_PATH


"""Создаем csv, записываем в него данные, проверяем их, удаляем файл"""


def test_work_with_csv():
    # Пишем файл
    with open(os.path.join(TEMP_PATH, 'new_csv.csv'), 'w', newline='') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=';')
        csvwriter.writerow(['Bonny', 'Born', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    TEMP_PATH_TO_CSV = os.path.join(TEMP_PATH, 'new_csv.csv')
    is_csv_exists = os.path.exists(TEMP_PATH_TO_CSV)
    assert is_csv_exists == True, 'Кажется, такого пути нет'
    print('Test 1 success')

    # Читаем получившийся файл и проверяем, что он записался, как надо

    with open(os.path.join(TEMP_PATH, 'new_csv.csv')) as csv_file:
        csvreader = csv.reader(csv_file, delimiter=';')
        result = []
        for row in csvreader:
            result.append(row)
            print(row)
        assert result[0] == ['Bonny', 'Born', 'Peter']
        assert result[1] == ['Alex', 'Serj', 'Yana']

    print('Full test success')
    # Подчищаем данные
    os.remove(os.path.join(TEMP_PATH, 'new_csv.csv'))  # либо сюда переменную TEMP_PATH_TO_CSV
