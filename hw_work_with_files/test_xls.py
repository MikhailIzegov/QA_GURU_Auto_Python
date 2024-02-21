import os
import xlrd

from hw_work_with_files.conftest import TEMP_PATH

# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_work_with_xls():
    book = xlrd.open_workbook(os.path.join(TEMP_PATH, 'import_ou_xls.xls'))

    print(f'Количество листов {book.nsheets}')
    print(f'Имена листов {book.sheet_names()}')
    sheet = book.sheet_by_index(0)
    print(f'Количество колонок  {sheet.ncols}')  # assert sheet.ncols ==
    print(f'Количество строк    {sheet.nrows}')  # assert sheet.nrows ==
    assert 'Департамент по работе с персоналом' in sheet.cell_value(rowx=3, colx=2), 'В этой ячейке другое значение'

    # Печатаем строки по очереди
    result = []
    for rx in range(sheet.nrows):
        result.append(sheet.row(rx))
    print(result)
    print(len(result)) # assert len(result) == 7, как и кол-во строк собственно


    # но если мы удалим, тест не воспроизведем снова, потому что мы не создаем в коде этот файл заново
    # os.remove(os.path.join(TEMP_PATH, 'import_ou_xls.xls'))

