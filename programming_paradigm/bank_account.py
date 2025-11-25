class BankAccount:

    def __init__(self, account_balance=0.0):
        if not isinstance(account_balance, (int, float)):
            raise TypeError("Initial balance must be a number")
        if account_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.account_balance = float(account_balance)

    def deposit(self, amount=50):
        if not isinstance(amount, (int, float)):
            return "Invalid amount"
        if amount <= 0:
            return "Deposit amount must be positive"
        self.account_balance += amount
        return f"Deposited: ${amount:.2f}"

    def withdraw(self, amount=20):
        if not isinstance(amount, (int, float)):
            return "Invalid amount"
        if amount <= 0:
            return "Withdrawal amount must be positive"
        if self.account_balance < amount:
            return "Insufficient funds"
        self.account_balance -= amount
        return f"Withdrew: ${amount:.2f}"

    def display_balance(self):
        return f"Current Balance: ${self.account_balance:.2f}"

    def __repr__(self):
        return f"BCurrent Balance: ${self.account_balance:.2f})"
