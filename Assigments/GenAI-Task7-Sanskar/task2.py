## Task-2

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

p1 = Product("Tablet","9000","Electronics")
p2 = Product("Phone", "20000", "Electronics")
print("Product p1 price: ",p1.get_price())
p1.set_price(6000)
print("New p1 price: ", p1.get_price())




    