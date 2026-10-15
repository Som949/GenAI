## Task-1
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        return f"Product Name: {self.name}, Price: Rs{self.price}, Category: {self.category}"

    def apply_discount(self, percent):
        discount_amount = self.price * (percent / 100)
        self.price -= discount_amount
        return f"Discount of {percent}% applied. New Price: Rs{self.price}"


p1 = Product("Gaming Laptop", 75000, "Electronics")
print(p1.get_info())

p2 = Product("Wireless Headphones", 1500, "Electronics")
print(p2.get_info())

print(p1.apply_discount(10))
print(p2.apply_discount(5))

