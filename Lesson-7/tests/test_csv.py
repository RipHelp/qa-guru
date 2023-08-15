import csv

# TODO оформить в тест, добавить ассерты и использовать универсальный путь
def test_csv():
    with open('resources/eggs.csv', 'x') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open('resources/eggs.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)

