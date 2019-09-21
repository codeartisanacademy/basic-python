import datetime

today = datetime.date.today()
now = datetime.datetime.now()

print(today)
print(now)

# the year 2012
print("The year is {0} ".format(today.year))

# the month is 09
print("The month is {month} ".format(month=today.month))

# the day is 14

next_new_year = datetime.date(year=2020, month=1, day=1)

print(next_new_year)

delta = next_new_year - today

print(type(delta))

print(delta.days)

print(delta.total_seconds())

print("new years is still {0} weeks and {1} days".format(int(delta.days/7), delta.days % 7))