#-------------------------------------------------
#------ Data and time => Introduction ------------
#-------------------------------------------------



import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))

# print the current date and time
print(datetime.datetime.now())

print("#" * 40)


# print the current year
print(datetime.datetime.now().year)

print("#" * 40)


# print the current month
print(datetime.datetime.now().month)

print("#" * 40)


# print the current day
print(datetime.datetime.now().day)
print("#" * 40)


# print start and end the date
print(datetime.datetime.min)
print(datetime.datetime.max)
print("#" * 40)


# print the current time
print(datetime.datetime.now().time())
print("#" * 40)

# print the current hour
print(datetime.datetime.now().time().hour)
print("#" * 40)

# print the current min
print(datetime.datetime.now().time().minute)
print("#" * 40)


# print the current second
print(datetime.datetime.now().time().second)
print("#" * 40)


# print start and end the date
print(datetime.time.min)
print(datetime.time.max)
print("#" * 40)
# print specific date
print(datetime.datetime(1982, 10, 23))
print(datetime.datetime(1982, 10, 23,23,45,30, 65443))
print("#" * 40)

my_Birthday = datetime.datetime(1993, 12, 15)
DateNow = datetime.datetime.now()

print(f"my birthday {my_Birthday} and Date now {DateNow} so i lived for {(DateNow- my_Birthday).days}")