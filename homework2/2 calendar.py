import calendar

d = int(input('Enter date '))
m = int(input('Enter month '))
y = int(input('Enter year '))

day = (calendar.weekday(y, m, d))
print(calendar.day_name[day])

x = calendar.day_name(input('Enter day'))
