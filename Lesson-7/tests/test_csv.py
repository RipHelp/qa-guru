import csv
import os
from os.path import join, dirname, exists, getsize

import pytest

file_name = 'eggs.csv'
file = join(dirname(__file__), file_name)


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
@pytest.fixture(autouse=True)
def create_csv():
    # Записываем данные в файл
    with open(file, 'w', newline='') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    yield

    os.remove(file)


def test_check_csv():
    # Проверяем записанный файл
    assert exists(file_name)


def test_read_csv():
    # Считываем данные из файла и проверяем их
    with open(file) as csv_file:
        csvreader = csv.reader(csv_file)
        for row in csvreader:
            print(row)
            assert len(row) == 3
            assert isinstance(row, list)

        assert getsize(file) == 34
