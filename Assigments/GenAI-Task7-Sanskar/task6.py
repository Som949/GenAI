##Task-6

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price
        self.category = category

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            raise ValueError("Price cannot be negative.")

    def get_info(self):
        return f"Product Name: {self.name}, Price: Rs{self.__price}, Category: {self.category}"

    def apply_discount(self, percent):
        discount_amount = self.__price * (percent / 100)
        self.__price -= discount_amount
        return f"Discount of {percent}% applied. New Price: Rs{self.__price}"

    def __str__(self):
        return f"Product Name: {self.name}, Price: Rs{self.__price}, Category: {self.category}"

    def __add__(self, other):
        return self.__price + other.__price

product1 = Product("Tablet", 10000, "Electronics")
product2 = Product("Phone", 25000, "Electronics")

print(product1)
print(product2)
print(product1 + product2)
