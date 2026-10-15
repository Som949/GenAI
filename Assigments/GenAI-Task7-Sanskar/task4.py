##Task-4
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

class Laptop(Product):
    def __init__(self, name, price, category):
        super().__init__(name, price, category)

    def get_info(self):
        return f"Product is {self.name} and its price is {self.get_price()}"

class Mobile(Product):
    def __init__(self, name, price, category):
        super().__init__(name, price, category)

    def get_info(self):
        return f"This Mobile is {self.name} and its price is {self.get_price()}"

Hp = Laptop("HP Victus", 60000, "Electronics")
Iphone = Mobile("Iphone 17", 90000, "Electronics")

for item in [Hp, Iphone]:
    print(item.get_info())

