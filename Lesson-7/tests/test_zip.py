import os
from zipfile import ZipFile
from os import path
from conftest import RESOURCES_DIR

my_zip = path.join(RESOURCES_DIR, 'hello.zip')


def test_zip():
    zip_ = ZipFile(my_zip)
    assert zip_.namelist()[0] == 'Hello.txt'

    text = zip_.read('Hello.txt')
    assert text in b'Hello world\n'
    zip_.close()

    with ZipFile(my_zip) as hellozip:
        hellozip.extract('Hello.txt')

    assert path.getsize(my_zip) == 128

    os.remove('Hello.txt')

