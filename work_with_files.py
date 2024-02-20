"""Это конспект с урока по работе с файлами"""

"""Идея создаст файл с сообщением Hello (по умолчанию мод - r, т.е. на чтение)"""
# open('hello', 'w').write('Hello')

"""Если вызовем ту же команду, только с другим сообщением внутри, то файл ПЕРЕЗАПИШЕТСЯ,
поэтому, чтобы дописать в конец файла инфу, используем мод a"""
# open('hello', 'a').write(' World')

"""'x' for creating and writing to a new file"""
# open('hello2', 'x').write('\nWorld')

"""'r' for reading. это плохая практика"""
# a = open('hello2')
# print(a.read())
# a.close()

"""хорошая практика, with автоматически закрывает файл"""
with open('work_with_files_and_paths/hello2.txt', 'w') as file:
    file.write('h')
