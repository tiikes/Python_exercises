year = 2005
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if is_leap_year(year):
    print("This is a leap year.")
else:
    print("This is not a leap year.")

    