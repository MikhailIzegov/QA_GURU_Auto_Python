class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError(f'Данного товара в кол-ве {quantity} нет')

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products.update({product: buy_count})

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if self.products.get(product) is None:
            raise ValueError(f'Данного товара {self.products.get(product)} нет в корзине')
        if product in self.products:
            if remove_count is None or remove_count > product.quantity:
                del self.products[product]
            else:
                self.products[product] -= remove_count

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        """
        Делаем код короче
        total_price = 0
        for item in self.products:
            total_price += item.price
        return total_price
        """
        if len(self.products) == 0:
            return 0
        else:
            return sum(item.price * amount for item, amount in self.products.items())
            # то есть self.products.items() пробегается по ключу-значению словаря, item - ключ, amount - значение,
            # а item.price берет цену из объекта класса Product

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        if len(self.products) == 0:
            raise 'Корзина пуста'
        for product in self.products:
            product.buy(self.products[product])
        self.products.clear()