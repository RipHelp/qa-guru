"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from models import Product, Cart


@pytest.fixture(scope="function")
def product_qa() -> Product:
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """
    @pytest.mark.parametrize('quantity, result', [(-10, ValueError),
                                                  (0, ValueError),
                                                  (10, True),
                                                  (1000, True),
                                                  (1001, False)])
    def test_product_check_quantity(self, product_qa: Product, quantity: int, result: bool or ValueError):
        # напишите проверки на метод check_quantity
        assert product_qa.check_quantity(quantity=quantity) == result, f"test_product_check_quantity не прошел."

    @pytest.mark.parametrize('quantity, result', [(100, 900),
                                                  (500, 500),
                                                  (1000, 0)])
    def test_product_buy(self, product_qa: Product, quantity: int, result: int):
        # напишите проверки на метод buy
        product_qa.buy(quantity=quantity)
        assert product_qa.quantity == result, (f"test_product_buy не прошел. Ожидаем {product_qa.quantity},"
                                               f" получили {result}")

    @pytest.mark.parametrize('quantity, result', [(1001, "ValueError"),
                                                  (100000, "ValueError")])
    def test_product_buy_more_than_available(self, product_qa: Product, quantity: int, result: int or ValueError):
        #  напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError) as exception:
            product_qa.buy(quantity)
        assert exception.typename == result


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
