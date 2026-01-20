#Build a BankAccount class with private balance. Allow deposit, withdrawal, and get_balance methods.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(5000)
print("Total Balance :" ,acc.get_balance())


#Output : 
#Total Balance : 6000
