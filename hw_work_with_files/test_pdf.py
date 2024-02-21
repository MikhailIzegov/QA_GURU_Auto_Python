import pypdf
import os

from hw_work_with_files.conftest import TEMP_PATH

# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_work_with_pdf():
    reader = pypdf.PdfReader(os.path.join(TEMP_PATH, 'Software Testing.pdf'))
    number_of_pages = len(reader.pages)
    page = reader.pages[50]
    first_page = reader.pages[0]
    text = page.extract_text()
    print(number_of_pages)
    # print(page)
    # print(text)
    assert number_of_pages == 303, 'Неверное кол-во страниц'
    assert 'Способы обнаружения проблем' in text, 'Возможно, это не та страница'

    count = 0
    for image_file in first_page.images:
        with open(os.path.join(TEMP_PATH, "pdf_image.png"), 'wb') as fp:  # Указали куда сохранять
            # и с каким названием
            fp.write(image_file.data)
            count += 1
    assert count == 1

    TEMP_PATH_TO_PDF = os.path.join(TEMP_PATH, 'pdf_image.png')
    is_pdf_exists = os.path.exists(TEMP_PATH_TO_PDF)
    assert is_pdf_exists, 'Такого файла, кажется нет'

    os.remove(TEMP_PATH_TO_PDF)
