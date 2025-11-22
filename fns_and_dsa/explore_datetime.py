from datetime import datetime, timedelta

def display_current_datetime(current_date=None):
    # Accepts an optional datetime; if none provided use now()
    if current_date is None:
        current_date = datetime.now()
    # Format to match the checker requirement
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")

def calculate_future_date(current_date):
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=number_of_days)
    formatted = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date: {formatted}")

def main():
    current_date = datetime.now()
    display_current_datetime()   
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()


