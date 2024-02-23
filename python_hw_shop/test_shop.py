"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from python_hw_shop.models import Product
from python_hw_shop.models import Cart


@pytest.fixture  # Относится к классу Product
def product_book():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture  # Относится к классу Cart
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product_book):
        # TODO напишите проверки на метод check_quantity
        assert product_book.check_quantity(product_book.quantity)

    def test_product_check_quantity_negative(self, product_book):
        # TODO напишите проверки на метод check_quantity
        assert product_book.check_quantity(product_book.quantity + 1) is False

    def test_product_buy(self, product_book):
        # TODO напишите проверки на метод buy
        initial_quantity = product_book.quantity
        product_book.buy(1)
        assert product_book.quantity == initial_quantity - 1
        product_book.buy(product_book.quantity)
        assert product_book.quantity == 0

    def test_product_buy_more_than_available(self, product_book):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        try:
            product_book.buy(product_book.quantity + 1)
        except ValueError as e:
            # Ожидаем, что выпадет исключение
            assert str(e) == f'Данного товара в кол-ве {product_book.quantity + 1} нет'
        else:
            assert False, 'Ожидалось получить исключение ValueError'


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_to_cart(self, product_book, cart):
        cart.add_product(product_book, 5)
        assert product_book in cart.products.keys(), 'Товар не добавился в корзину'

    def test_remove_from_cart(self, product_book, cart):
        cart.add_product(product_book, 5)
        initial_count = cart.products.get(product_book)
        cart.remove_product(product_book, 1)
        assert cart.products.get(product_book) == initial_count - 1

    def test_clear_cart(self, product_book, cart):
        cart.add_product(product_book, 5)
        cart.clear()
        assert len(cart.products) == 0, 'Корзина не пуста'

    def test_get_total_price(self, product_book, cart):
        cart.add_product(product_book, 5)
        total = cart.get_total_price()
        print(total)

    def test_buy_from_cart(self, product_book, cart):
        initial_quantity = product_book.quantity
        amount_to_buy = 5
        cart.add_product(product_book, amount_to_buy)
        cart.buy()
        assert len(cart.products) == 0
        assert product_book.quantity == initial_quantity - amount_to_buy
