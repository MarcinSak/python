# BAD Example
class BadPaymentService:
    def process_payment(self, amount):
        try:
            print(f"Processing payment of {amount}")
        except Exception as e:
            self.log_error(e)

    def log_error(self, error):
        print(f"Error: {error}")

# ---

class PaymentService:
    def __init__(self, logger):
        self.logger = logger
    
    def process_payment(self, amount):
        try:
            print(f"Processing payment of {amount}")
        except Exception as e:
            self.logger.log_error(e)

class Logger:
    def log_error(self, error):
        print(f"Error: {error}")

logger = Logger()
payment_service = PaymentService(logger)
payment_service.process_payment(100)

