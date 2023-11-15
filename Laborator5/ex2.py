class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Mai baga bani, nu ai destui smechere")

    def calculate_interest(self):
        pass


class SavingsAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def calculate_interest(self):
        interest = self.balance * 0.05
        self.balance += interest


class CheckingAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def calculate_interest(self):
        interest = self.balance * 0.01
        self.balance += interest


def main():
    savings_account = SavingsAccount(1112, 1000)
    checking_account = CheckingAccount(3421, 500)

    savings_account.deposit(500)
    savings_account.withdraw(200)
    savings_account.calculate_interest()

    checking_account.deposit(1000)
    checking_account.withdraw(200)
    checking_account.calculate_interest()

    print(f"Banii din Savings Account: {savings_account.balance}")
    print(f"Banii din Checking Account: {checking_account.balance}")


main()
