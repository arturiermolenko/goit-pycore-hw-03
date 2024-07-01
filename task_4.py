from datetime import datetime, timedelta


def get_upcoming_birthdays(users_list: list[dict]) -> list[dict]:
    """
    This function is used to retrieve a list of users who have their birthdays coming up
    in the next 7 days, including today.
    :param users_list: list dictionaries of users and their birthdays
    :return: list of dictionaries of users and their birthdays,
    that have their upcoming birthdays
    """
    congratulation_list = []
    date_today = datetime.today().date()

    for user in users_list:
        datetime_obj = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        user_name = user["name"]

        if date_today <= datetime_obj <= date_today + timedelta(days=7):
            if datetime_obj.weekday() == 5:
                congratulation_date = datetime_obj + timedelta(days=2)
            elif datetime_obj.weekday() == 6:
                congratulation_date = datetime_obj + timedelta(days=1)
            else:
                congratulation_date = datetime_obj

            congratulation_date = congratulation_date.strftime("%Y.%m.%d")
            users_info = {
                "name": user_name,
                "congratulation_date": congratulation_date,
            }
            congratulation_list.append(users_info)

    return congratulation_list


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Artur", "birthday": "2024.07.03"},
    ]
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("This week we congratulate:", upcoming_birthdays)
