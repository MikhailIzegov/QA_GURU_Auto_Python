# Необходимо предустановить pip3 install pypdf
import pypdf

reader = pypdf.PdfReader('resource/Software Testing.pdf')
number_of_pages = len(reader.pages)
print(number_of_pages)
first_page = reader.pages[0]
print(first_page)
text = first_page.extract_text()
print(text)


# Для извлечения изображение дополнительно устанавливаем pip3 install pypdf[image]
count = 0
for image_file in first_page.images:
    with open(str(count) + image_file.name, "wb") as fp:
        fp.write(image_file.data)
        count += 1
