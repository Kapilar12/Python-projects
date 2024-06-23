class BalanceException(Exception):
    pass
class CreateBankAccount:
    def __init__(self, initialamount, account_name):
        self.balance = initialamount
        self.name = account_name
        print(
            f"\nYour Account '{self.name}' created successfully.\nBalance = Rs {self.balance}")

    def fetch_balance(self):
        print(f"\nAccount '{self.name}' balance = Rs {self.balance}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.fetch_balance()

    def valid_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\n Insufficient Balance\n'{self.name}'balance = ${self.balance}"
            )

    def withdraw(self, amount):
        try:
            self.valid_transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw completed.")
            self.fetch_balance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    def transfer(self, amount, account):
        try:
            print('\nBeginning Transfer..Wait for a while')
            self.valid_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer completed!')
        except BalanceException as error:
            print(f'\nTransfer interrupted.  {error}')
