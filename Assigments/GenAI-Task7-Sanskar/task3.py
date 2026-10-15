## Task-3

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

class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years

    def get_info(self):
        return super().get_info() + ", " + f"Warranty years: {self.warranty_years}"


ep1 = ElectronicProduct("Smart TV", 50000, "Electronics", 2)
print(ep1.get_info())

    
