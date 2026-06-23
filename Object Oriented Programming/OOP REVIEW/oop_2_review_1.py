# Day 48 - OOP Review Topic 2: Class Variables vs Instance Variables


class BankAccount:
    bank_name = "PyBank"
    total_accounts = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1

    def get_info(self):
        print(f"Bank Name: {self.bank_name}, Total Accounts: {self.total_accounts}")

acc1 = BankAccount('SiSU', 2000000)
acc2 = BankAccount('Lana', 200000)

acc1.get_info()
acc2.get_info()