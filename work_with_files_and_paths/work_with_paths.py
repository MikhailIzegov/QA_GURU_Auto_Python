import os

"""Узнаем абсолютный путь файла по его имени"""
abs_path = os.path.abspath('hello')
print(abs_path)

"""Абсолютный путь директории, в которой лежит файл. 
dirname лучше искать от абсолютного пути, тогда от него можно будет ходить куда угодно"""
print(os.path.dirname(abs_path))

"""Абсолютный путь директории c текущим файлом и к проекту"""
CURRENT_FILE_PATH = os.path.dirname(__file__)
print(CURRENT_FILE_PATH)
PROJECT_ROOT_PATH = os.path.dirname(CURRENT_FILE_PATH)
print(PROJECT_ROOT_PATH)

"""На Windows ЭТО НЕ РАБОТАЕТ: 
FileNotFoundError: [Errno 2] No such file or directory"""

# anyfile_path = os.path.abspath('./resource/anyfile')
# print(anyfile_path)
# with open(anyfile_path) as file:
#     print(file.read())

"""Склеиваем пути. Вот, что сработает, развернет слэши в правильную сторону для винды"""
anyfile_path = os.path.join(PROJECT_ROOT_PATH, 'resource', 'anyfile')
print(anyfile_path)
with open(anyfile_path) as file:
    print(file.read())

"""Еще пример как постучаться к какому-то файлу"""
joined_path = os.path.join(PROJECT_ROOT_PATH, '..', 'hello')  # Напечатается с точками в консоли
print(joined_path)
print(os.path.abspath(joined_path))  # А вот так без точек напечатается тот же самый путь


"""Проверка, что такой путь есть"""
resource_path = os.path.join(PROJECT_ROOT_PATH, 'resource')
print(resource_path)
is_resource_exists = os.path.exists(resource_path)
print(is_resource_exists)  # Вернет True

"""Можно еще написать условие, что если такой нет директории, то ее надо создать"""
# if not is_resource_exists:
#     os.mkdir('new_resource')



