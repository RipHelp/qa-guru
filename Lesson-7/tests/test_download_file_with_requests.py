import os.path
import requests
from conftest import RESOURCES_DIR

# Оформить в тест, добавить ассерты, сохранять и читать из tmp, использовать универсальный путь
url = 'https://selenium.dev/images/selenium_logo_square_green.png'
path = os.path.join(RESOURCES_DIR, 'selenium_logo.png')


def test_download_with_requests():
    response = requests.get(url)

    assert response.status_code == 200

    with open(path, 'wb') as file:
        file.write(response.content)

    size = os.path.getsize(path)

    assert size == 30803

    os.remove(path)
