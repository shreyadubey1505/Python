# There is agreat logic -based questions for students...


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_months(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]


while True:
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    if 1 <= month <= 12:
        days = days_in_months(year, month)
        print(("The Number of days in the month is:"), days)
        break
    else:
        print("Invalid month. Please enter a month between 1 and 12.")
