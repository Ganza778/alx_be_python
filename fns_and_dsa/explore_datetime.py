from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date

def calculate_future_date(current_date):
    try:
        num_days = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=num_days)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    current = display_current_datetime()
    calculate_future_date(current)
