#Make a class BankAccount with deposit() and withdraw() methods and balance tracking.
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

account = BankAccount(1000)  # Initial balance of 1000
account.deposit()
account.withdraw()
