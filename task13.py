class Payment:
    def pay(self, a):
        pass

class PayPalPayment(Payment):
    def pay(self, a):
        print(f"Paid {a} using PayPal")

class CardPayment(Payment):
    def pay(self, a):
        print(f"Paid {a} using Card")

p1 = PayPalPayment()
p2 = CardPayment()
p1.pay(100)
p2.pay(200)
