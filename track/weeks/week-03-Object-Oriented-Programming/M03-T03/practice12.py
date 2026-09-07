# Build BankAccount and SavingsAccount using Super()

class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder

    def show_holder(self):
        return f"Account Holder: {self.account_holder}"


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance):
        # Call the parent constructor
        # Store balance
        super().__init__(account_holder)
        self.balance = balance

    def show_balance(self):
        # Return the balance
        return f"Balance: {self.balance}"


name = input()
balance = int(input())

account = SavingsAccount(name, balance)

print(account.show_holder())
print(account.show_balance())