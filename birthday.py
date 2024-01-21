import datetime

def calculate_days_left():
    
    birthday_str = input("Enter your birthday (YYYY-MM-DD): ")

    birthday = datetime.datetime.strptime(birthday_str, "%Y-%m-%d").date()

    today = datetime.date.today()

    next_birthday = datetime.date(today.year, birthday.month, birthday.day)

    if next_birthday < today:

        next_birthday = datetime.date(today.year + 1, birthday.month, birthday.day)

    days_left = (next_birthday - today).days

    print("There are", days_left, "days left until your next birthday!")

calculate_days_left()


