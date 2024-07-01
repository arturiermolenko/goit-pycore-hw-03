import re
from datetime import datetime


def get_days_from_today(date: str) -> int | None:
    """
    Function calculates the number of days between the given date and the current date
    :param date: the date to calculate the number of days from
    :return: the number of days between the given date and the current date
    """
    pattern = r"\d{4}\-\d{2}\-\d{2}"
    if not re.match(pattern=pattern, string=date):
        print("Invalid date format. Date should be in format YYYY-MM-DD")
        return

    try:
        daytime_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Date should be real")
        return

    current_date = datetime.today()
    days = current_date - daytime_date

    return days.days


if __name__ == "__main__":
    date_input = input("Enter a date in format YYYY-MM-DD: ")
    result = get_days_from_today(date_input)
    if result:
        print(f"Number of days from today: {result}")
