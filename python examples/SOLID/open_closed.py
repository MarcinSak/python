class BadTransactionProcessor:
    def process(self, transaction_type, amount):
        if transaction_type == "credit":
            self.process_credit(amount)
        elif transaction_type == "debit":
            self.process_debit(amount)
        else:
            raise ValueError("Unknown transaction type")
    
    def process_credit(self, amount):
        print(f"Processing credit of {amount}")
    
    def process_debit(self, amount):
        print(f"Processing debit of {amount}")

# ---

from abc import ABC, abstractmethod
from random import randint

class Transaction(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class CreditTransaction(Transaction):
    def process(self, amount):
        print(f"Processing credit of {amount}")

class DebitTransaction(Transaction):
    def process(self, amount):
        print(f"Processing debit of {amount}")

class TransactionProcessor:
    def __init__(self, transaction: Transaction):
        self.transaction = transaction
    
    def process(self, amount):
        self.transaction.process(amount)

transactions = [CreditTransaction(), DebitTransaction()]
for transaction in transactions:
    random_number = randint(1,101)    
    processor = TransactionProcessor(transaction)
    processor.process(random_number)