# Banking Management System Program using Python OOP's
import datetime

class Account:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        print(f"Account is created for {self.name}")

    def deposite(self, amount):
        if amount > 0:
            amount += amount
            print(f"{self.amount} added on {datetime.datetime.now()}")

    def withdraw(self, amount):
        if amount > 0:
            amount -= amount
            print(f"{self.amount} debit on {datetime.datetime.now()}")
    

    def show_balance(self):
        print(f"{self.name} account balance is {self.amount}")

Amit = Account('Amit',20)
Amit.show_balance()
Amit.deposite(20)
