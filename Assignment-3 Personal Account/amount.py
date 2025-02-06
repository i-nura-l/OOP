from datetime import datetime

class Amount:
    # constructor - special method to initialize attributes
    def __init__(self, amount, transaction_type:str):
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

    def __str__(self):
        return f"Amount: {self.amount:.2f}, Time: {self.timestamp}, Type: {self.transaction_type}"
