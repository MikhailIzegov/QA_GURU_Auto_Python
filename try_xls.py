# Нужно предустановить pip3 install xlrd
import xlrd


book = xlrd.open_workbook('resource/import_ou_xls.xls')

print(f'Кол-во листов {book.nsheets}')
print(f'Имена листов {book.sheet_names()}')

"""Работаем с листом, индекс с нуля"""
sheet = book.sheet_by_index(0)
print(f'Кол-во колонок {sheet.ncols}')
print(f'Кол-во колонок {sheet.nrows}')
print(f'Пересечение строки и столбца {sheet.cell_value(rowx=2, colx=1)}')

"""Печатаем все строки по очереди"""

for rx in range(sheet.nrows):
    print(sheet.row(rx))