import os
import zipfile

from hw_work_with_files.conftest import TEMP_PATH


def test_check_files_in_zip():
    # Смотрим, какие файлы есть в temp
    files_in_temp = os.listdir(TEMP_PATH)
    print(files_in_temp)

    # Список файлов в temp, который будем архивировать
    files_to_archive = [
         'anyfile',
         'eggs.csv',
         'import_ou_xls.xls',
         'import_ou_xlsx.xlsx',
         'Software Testing.pdf'
    ]

    # Путь к файлу архива
    zip_filename = os.path.join(TEMP_PATH, 'archive_for_test.zip')

    # Создаем архив
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file_name in files_to_archive:
            file_path = os.path.join(TEMP_PATH, file_name)
            zipf.write(file_path, file_name)

    # Открываем архив
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        # Проверяем, что каждый файл в архиве существует
        files_to_archive = [
         'anyfile',
         'eggs.csv',
         'import_ou_xls.xls',
         'import_ou_xlsx.xlsx',
         'Software Testing.pdf'
        ]
        for file_name in files_to_archive:
            assert file_name in zipf.namelist()

    print('Successful test!')

"""Решение другого человека:
def test_zip_file():
    with zipfile.ZipFile(os.path.join(RESOURCES_DIR, 'file_hello.zip')) as zip_file:
        zip_file.extract('file_hello.txt', path=RESOURCES_DIR)
        name_list = zip_file.namelist()
        print(name_list)
        text = zip_file.read('file_hello.txt')
        print(text)
        assert 'file_hello.txt' in name_list
        assert text == b'Hello'
        assert os.path.isfile(os.path.join(RESOURCES_DIR, 'file_hello.txt'))

        os.remove(os.path.join(RESOURCES_DIR, 'file_hello.txt'))"""