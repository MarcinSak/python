class BadAccount:
    def withdraw(self, amount):
        print(f"Withdrawing {amount} from account")

class BadSavingsAccount(BadAccount):
    def withdraw(self, amount):
        if amount > 1000:
            raise ValueError("Cannot withdraw more than 1000 from savings account")
        super().withdraw(amount)

#---

from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

class CheckingAccount(Account):
    def withdraw(self, amount):
        print(f"Withdrawing {amount} from checking account")

class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount > 1000:
            raise ValueError("Cannot withdraw more than 1000 from savings account")
        print(f"Withdrawing {amount} from savings account")

def process_withdrawal(account: Account, amount):
    account.withdraw(amount)

savings_account = SavingsAccount()
checking_account = CheckingAccount()

process_withdrawal(savings_account, 500)
process_withdrawal(checking_account, 1500)
