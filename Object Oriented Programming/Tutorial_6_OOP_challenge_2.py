# ============================================================
# OOP - Property Decorators: Challenge 2
# Topic   : @property, setter, validation, raise, __repr__
# Day     : 27
# ============================================================


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
    
    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"


acc = BankAccount('Mehmet', 1000000)
print(acc)               # BankAccount(owner='John', balance=1000)

acc.deposit(500)
print(acc.balance)       # 1500

acc.withdraw(200)
print(acc.balance)       # 1300

try:
    acc.withdraw(9999)
except ValueError as e:
    print(e)             # Insufficient funds

try:
    acc.balance = -50
except ValueError as e:
    print(e)             # Balance cannot be negative