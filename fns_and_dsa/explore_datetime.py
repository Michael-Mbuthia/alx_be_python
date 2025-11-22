from datetime import datetime, timedelta

def display_current_datetime(current_date=None):
    # Accepts an optional datetime; if none provided use now()
    if current_date is None:
        current_date = datetime.now()
    print(f"Current date and time: {current_date}")

def future_date(current_date):
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future date: {future_date}")

def main():
    current_date = datetime.now()
    display_current_datetime()   
    future_date(current_date)

if __name__ == "__main__":
    main()


