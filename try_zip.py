import zipfile

zip_file = zipfile.ZipFile('resource/hello.zip')
print(zip_file.namelist())  # Смотрим, какие файлы в архиве
text = zip_file.read('Hello.txt')  # Читаем файл, НЕ распаковывая его
print(text)
zip_file.close()  # Не забываем закрыть, но лучше использовать with

"""Перекидываем Hello.txt в корень проекта, но у него есть аргумент path, можно указать, куда экстрактить"""
with zipfile.ZipFile('resource/hello.zip') as hellozip:
    hellozip.extract('Hello.txt')