import sys
from bank_account import BankAccount


def main():
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = None
    if params:
        try:
            amount = float(params[0])
        except ValueError:
            print("Invalid amount.")
            sys.exit(1)

    if command == "deposit" and amount is not None:
        result = account.deposit(amount)
        print(result)
    elif command == "withdraw" and amount is not None:
        result = account.withdraw(amount)
        print(result)
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()