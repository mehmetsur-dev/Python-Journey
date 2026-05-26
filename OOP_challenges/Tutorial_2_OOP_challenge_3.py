# ============================================================
# OOP Class Variables — Challenge 3
# Topic: Class variables, instance variables, methods
# Day 23 — Corey Schafer OOP Tutorial 2
# Author: Mehmet Sur
# Date: 26.05.2026
# ============================================================


class BankAccount:
    bank_name = "FillMe"
    interest_rate = 0.05
    total_account = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        BankAccount.total_account += 1

    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds!")
        else:
            self.balance -= amount

    def apply_interest(self):
        self.balance = int(self.balance + (self.balance * self.interest_rate))

    def update_interest_rate(self, new_rate):
        BankAccount.interest_rate = new_rate


# --- Create accounts ---
owr1 = BankAccount("Mehmet", 1000000)
owr2 = BankAccount("Murad", 10000000)

# --- Total accounts ---
print(BankAccount.total_account)        # 2

# --- Deposit ---
owr1.deposit(50000)
print(owr1.balance)                     # 1050000

# --- Withdraw ---
owr2.withdraw(1000000)
print(owr2.balance)                     # 9000000

# --- Insufficient funds ---
owr1.withdraw(10000000)                 # Insufficient funds!

# --- Apply interest ---
print(owr1.balance)                     # before
owr1.apply_interest()
print(owr1.balance)                     # after

print(owr2.balance)                     # before
owr2.apply_interest()
print(owr2.balance)                     # after

# --- Update interest rate for ALL accounts ---
owr1.update_interest_rate(0.10)
print(owr1.interest_rate)               # 0.10
print(owr2.interest_rate)               # 0.10 — proves all accounts updated