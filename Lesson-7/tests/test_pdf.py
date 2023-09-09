from pypdf import PdfReader
from os import path
from conftest import RESOURCES_DIR

# Оформить в тест, добавить ассерты и использовать универсальный путь
my_pdf = path.join(RESOURCES_DIR, "docs-pytest-org-en-latest.pdf")


def test_read_pdf():
    reader = PdfReader(my_pdf)
    number_of_pages = len(reader.pages)
    print(number_of_pages)

    assert path.getsize(my_pdf) == 1739253

    assert number_of_pages == 412

    page = reader.pages[0]
    text = page.extract_text()
    print(text)

    assert "Release 0.1" in text


