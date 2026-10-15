
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price
        self.category = category

    def get_price(self):
        return self.__price

    def get_info(self):
        return f"Name: {self.name}, Price: Rs.{self.__price}, Category: {self.category}"

    def __add__(self, other):
        return self.__price + other.__price


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        self.products = [
            product for product in self.products
            if product.name != name
        ]

    def get_total_value(self):
        return sum(product.get_price() for product in self.products)

    def show_all_products(self):
        for product in self.products:
            print(product.get_info())


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        category = input("Enter product category: ")

        product = Product(name, price, category)
        self.inventory.add_product(product)

    def show_summary(self):
        print(f"\nStore Name: {self.store_name}")
        print("All Products:")
        self.inventory.show_all_products()

        print("Total Items:", len(self.inventory.products))
        print("Total Inventory Value: Rs.",
              self.inventory.get_total_value())


store = Store("Local General Store")

store.inventory.add_product(Product("Laptop", 80000, "Electronics"))
store.inventory.add_product(Product("Mouse", 500, "Accessories"))
store.inventory.add_product(Product("Keyboard", 800, "Accessories"))
store.show_summary()

p1 = Product("Laptop", 80000, "Electronics")
p2 = Product("Mouse", 500, "Accessories")

print("\nCombined Price:", p1 + p2)
