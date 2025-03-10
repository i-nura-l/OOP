from amount import Amount

class PersonalAccount:
    def __init__(self, account_number:int, account_holder:str, __balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        transaction = Amount(amount, "DEPOSIT")
        self.transactions.append(transaction)
        print('Deposit:',amount, ', Balance:', self.__balance)

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            transaction = Amount(amount, "WITHDRAWAL")
            self.transactions.append(transaction)
            print('Withdraw: ', amount, ', Balance:', self.__balance)
        else:
            print('Withdraw: ', amount, ', Not enough balance.')

    def print_transaction_history(self):
        if not self.transactions:
            print("No transactions available.\n")
        else:
            for transaction in self.transactions:
                print(transaction)

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_holder(self):
        return self.account_holder

    def set_account_holder(self, account_holder):
        self.account_holder = account_holder

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Account Number: {self.account_number}, Balance: ${self.__balance:.2f}"

    def __add__(self, amount):
        self.deposit(amount)
        return self

    def __sub__(self, amount):
        self.withdraw(amount)
        return self