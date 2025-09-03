class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance  

    def deposit(self, a):
        self.balance += a

    def withdraw(self, a):
        if a <= self.balance:
            self.balance -= a

    def get_balance(self):
        return self.balance

acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.get_balance())
