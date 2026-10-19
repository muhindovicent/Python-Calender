import datetime
import sys

def is_leap(year: int) -> bool:
    """Return True if year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year: int, month: int) -> int:
    """Return number of days in given month (1=January ... 12=December)."""
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    else:  # February
        return 29 if is_leap(year) else 28

def get_start_weekday(year: int, month: int) -> int:
    """
    Return the weekday of the 1st day of the month.
    Returns 0 = Monday, 1 = Tuesday, ..., 6 = Sunday.
    Uses Python's datetime module for correctness.
    """
    return datetime.date(year, month, 1).weekday()  # Monday=0 ... Sunday=6

def display_month(year: int, month: int, first_sunday: bool = True) -> None:
    """
    Print a formatted calendar for the given month and year.
    If first_sunday is True, weeks start on Sunday, otherwise Monday.
    """
    # Get month name
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    month_name = month_names[month - 1]

    # Header
    print(f"\n{month_name} {year}".center(20))
    print("Su Mo Tu We Th Fr Sa" if first_sunday else "Mo Tu We Th Fr Sa Su")
    print("-" * 20)

    # Calculate calendar grid
    days = days_in_month(year, month)
    # weekday of 1st day: Monday=0 ... Sunday=6
    start_weekday = get_start_weekday(year, month)

    # Convert to Sunday-based offset if needed
    if first_sunday:
        # Monday=0 -> Sunday offset: (0+1)%7 = 1, (6+1)%7=0 (Sunday)
        start_offset = (start_weekday + 1) % 7
    else:
        # Monday-based: offset is start_weekday (0=Monday)
        start_offset = start_weekday

    # Print initial blanks
    line = []
    for _ in range(start_offset):
        line.append("  ")

    # Print days
    for day in range(1, days + 1):
        line.append(f"{day:2d}")
        if len(line) == 7:
            print(" ".join(line))
            line = []

    # Print remaining days in last line
    if line:
        # Fill blanks to keep alignment (optional)
        while len(line) < 7:
            line.append("  ")
        print(" ".join(line))

def display_year(year: int, first_sunday: bool = True) -> None:
    """Print calendars for all months of the given year."""
    print(f"\n{'=' * 34}\n      CALENDAR {year}\n{'=' * 34}")
    for month in range(1, 13):
        display_month(year, month, first_sunday)
        if month % 3 == 0 and month != 12:
            input("Press Enter to continue...")

def current_month_calendar() -> None:
    """Display calendar for the current month and year."""
    today = datetime.date.today()
    display_month(today.year, today.month)

def main() -> None:
    """Interactive calendar program."""
    while True:
        print("\n--- Calendar Menu ---")
        print("1. Show calendar for a specific month and year")
        print("2. Show calendar for current month")
        print("3. Show calendar for an entire year")
        print("4. Exit")
        choice = input("Your choice (1-4): ").strip()

        if choice == '1':
            try:
                year = int(input("Enter year (e.g., 2026): "))
                month = int(input("Enter month (1-12): "))
                if month < 1 or month > 12:
                    print("Month must be between 1 and 12.")
                    continue
                display_month(year, month)
            except ValueError:
                print("Invalid input. Please enter numbers.")
        elif choice == '2':
            current_month_calendar()
        elif choice == '3':
            try:
                year = int(input("Enter year: "))
                display_year(year)
            except ValueError:
                print("Invalid year.")
        elif choice == '4':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please choose 1-4.")

if __name__ == "__main__":
    main()