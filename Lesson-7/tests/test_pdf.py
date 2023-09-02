from pypdf import PdfReader
from os import path
from conftest import RESOURCES_DIR

# Оформить в тест, добавить ассерты и использовать универсальный путь
my_pdf = path.join(RESOURCES_DIR, "docs-pytest-org-en-latest.pdf")


def test_read_pdf():
    reader = PdfReader(my_pdf)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)