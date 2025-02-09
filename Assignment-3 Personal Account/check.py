from amount import Amount
from personal import PersonalAccount

if __name__ == '__main__':
    a = Amount(23, 'DEPOSIT')
    print(a)

    account = PersonalAccount(123456, "Nurali")
    print(account, '\n')

    account.deposit(500)
    account.withdraw(200)

    print("Current Balance:", account.get_balance())
    print("Transaction History:")
    account.print_transaction_history()


    print()
    account.set_account_holder("New Holder")
    print(account,'\n')

    print(account.get_balance())
    print(account.get_account_holder())
    print(account.get_account_number())

    print(account.__str__(), '\n')
    print(account.__add__(200), '\n')
    print(account.__sub__(200), '\n')

