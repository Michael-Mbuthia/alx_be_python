from datetime import datetime, timedelta

def display_current_datetime(current_date):
    print(f"Current date and time: {current_date}")

def future_date(current_date):
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    new_date = current_date + timedelta(days=number_of_days)
    print(f"Future date: {new_date}")

def main():
    current_date = datetime.now()
    display_current_datetime(current_date)
    future_date(current_date)

if __name__ == "__main__":
    main()


