x = int(input('Enter number '))

sum = 0

for i in range(x):
    y = int(input('enter number %d ' % (i + 1)))
    if y % 3 == 0:
        sum += y
print(sum)
