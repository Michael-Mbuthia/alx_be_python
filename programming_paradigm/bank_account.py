class BankAccount:

    def __init__(self, account_balance=0.0):
        if account_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.account_balance = float(account_balance)

    def deposit(self, amount=50):
        if amount <= 0:
            return "Deposit amount must be positive"
        else:
            self.account_balance += amount
            return f"Deposited: ${amount}"

    def withdraw(self, amount=20):
        if amount <= 0:
            return "Withdrawal amount must be positive"
        if amount > self.account_balance:
            return "Insufficient funds."
        self.account_balance -= amount
        return f"Withdrew: ${amount}"

    def display_balance(self):
        # Print the balance so tests that capture stdout receive the expected output
        msg = f"Current Balance: ${self.account_balance:.2f}"
        print(msg)
        return msg