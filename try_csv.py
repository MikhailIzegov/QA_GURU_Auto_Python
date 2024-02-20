import csv


"""
CSV - Comma Separated Values
"""

with open('./resource/eggs.csv') as csv_file:
    csvreader = csv.reader(csv_file)
    for row in csvreader:
        print(row)

"""Создаем свой csv-файл"""
with open('./resource/new_csv.csv', 'w', newline='') as csv_file:
    csvwriter = csv.writer(csv_file, delimiter=';')
    csvwriter.writerow(['Bonny', 'Born', 'Peter'])
    csvwriter.writerow(['Alex', 'Serj', 'Yana'])

"""Читаем наш новый csv-файл"""
with open('./resource/new_csv.csv') as csv_file:
    csvreader = csv.reader(csv_file)
    for row in csvreader:
        print(row)



