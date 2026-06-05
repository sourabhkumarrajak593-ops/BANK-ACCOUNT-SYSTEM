class BankAccount:

    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount
        print("Deposited: ", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn: ", amount)
        else:
            print("Insufficient Balance!")

    def check_balance(self):
        print("Current Balance: ", self.balance)

    

    


account_number = input("Enter Bank Account Number: ")
owner_name = input("Enter Owner Name: ")
balance = float(input("Enter Initial Balance: "))
acc = BankAccount(account_number, owner_name, balance)

amount = float(input("Enter Deposit Amount: "))
acc.deposit(amount)

amount = float(input("Enter Withdraw Amount: "))
acc.withdraw(amount)

acc.check_balance()



