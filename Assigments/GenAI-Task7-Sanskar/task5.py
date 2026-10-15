## Task5

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of Rs{amount}")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of Rs{amount}")

pay1 = CreditCardPayment()
pay1.process_payment(5000)

pay2 = UPIPayment()
pay2.process_payment(2000)


