from datetime import datetime


def read_employees_from_file(users):
    today = datetime.today().date()
    birthdays = {}
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        if (birthday_this_year - today).days < 7:
            day_of_week = GetNameOfDay(birthday_this_year)
            if day_of_week in birthdays:
                birthdays[day_of_week].append(name)
            else:
                birthdays[day_of_week] = [name]
    result = ""
    for day, names in birthdays.items():
        result += f"{day} {', '.join(names)}\n"

    return result


def GetNameOfDay(date):
    return date.strftime('%A')


if __name__ == "__main__":
    print(read_employees_from_file([
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
        {"name": "Kalle", "birthday": datetime(1992, 10, 28)},
        {"name": "Steve Jobs", "birthday": datetime(1955, 10, 28)},
        {"name": "Anelia", "birthday": datetime(1996, 10, 29)}
    ]))
