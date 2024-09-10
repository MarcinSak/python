class InsufficientFundsError(Exception):
    pass

class InvalidTransactionError(Exception):
    pass

class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidTransactionError("Deposit amount must be greater than zero.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidTransactionError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for this withdrawal.")
        self.balance -= amount
        return self.balance

class BankTransaction:
    def __init__(self, account: Account):
        self.account = account

    def process_deposit(self, amount):
        try:
            return self.account.deposit(amount)
        except InvalidTransactionError as e:
            print(f"Transaction error: {e}")
            raise

    def process_withdrawal(self, amount):
        try:
            return self.account.withdraw(amount)
        except InsufficientFundsError as e:
            print(f"Transaction error: {e}")
            raise
        except InvalidTransactionError as e:
            print(f"Transaction error: {e}")
            raise

def perform_transaction():
    customer_account = Account(100)
    transaction_processor = BankTransaction(customer_account)

    try:
        print(f"Balance after deposit: {transaction_processor.process_deposit(50)}")
        print(f"Balance after withdrawal: {transaction_processor.process_withdrawal(100)}")
    except InsufficientFundsError:
        print("Transaction failed due to insufficient funds.")
    except InvalidTransactionError:
        print("Invalid transaction detected.")
    finally:
        print(f"Final balance: {customer_account.balance}")

if __name__ == "__main__":
    perform_transaction()
