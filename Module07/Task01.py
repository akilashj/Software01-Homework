def get_season(month):
    """Return the season name for the given month number."""
    if month in (12, 1, 2):
        return "winter"
    elif month in (3, 4, 5):
        return "spring"
    elif month in (6, 7, 8):
        return "summer"
    elif month in (9, 10, 11):
        return "autumn"
    else:
        return None

try:
    month_number = int(input("Enter the number of a month (1-12): "))
    print(f"You entered: {month_number}")

    season = get_season(month_number)
    if season:
        print(f"The season is {season}.")
    else:
        print("Please enter a number between 1 and 12.")
except ValueError:
    print("Please enter a number between 1 and 12.")