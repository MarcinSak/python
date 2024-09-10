class BadPayPalPayment:
    def make_payment(self, amount):
        print(f"Making payment of {amount} via PayPal")

class BadPaymentProcessor:
    def process_payment(self, amount):
        payment = BadPayPalPayment()
        payment.make_payment(amount)

#---

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class PayPalPayment(PaymentMethod):
    def make_payment(self, amount):
        print(f"Making payment of {amount} via PayPal")

class CreditCardPayment(PaymentMethod):
    def make_payment(self, amount):
        print(f"Making payment of {amount} via Credit Card")

class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method
    
    def process_payment(self, amount):
        self.payment_method.make_payment(amount)

paypal_payment = PayPalPayment()
processor = PaymentProcessor(paypal_payment)
processor.process_payment(100)
