class BankAccount():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f"Account owner:   {self.owner}\nAccount balance: ${self.balance}"
    def deposit(self, amount):
        self.balance += amount
        print("Deposit Accepted")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable!")
    

jose_account = BankAccount("Jose", 100)
print(jose_account)
print(jose_account.owner)
print(jose_account.balance)

jose_account.deposit(50)
print(jose_account.balance)
jose_account.withdraw(75)
print(jose_account.balance)
jose_account.withdraw(500)
print(jose_account.balance)
