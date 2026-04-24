class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def total_price(self):
        return sum(item.price for item in self.items)

    def show_cart(self):
        for item in self.items:
            print(f"{item.name} - {item.price}")
        print("Jami:", self.total_price())


# Test
p1 = Product("Phone", 500)
p2 = Product("Laptop", 1000)

cart = Cart()
cart.add_product(p1)
cart.add_product(p2)

cart.show_cart()
