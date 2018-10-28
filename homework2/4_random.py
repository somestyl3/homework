import random

x = random.randrange(1, 10)
y = int(input('enter your number '))

while True:
    if x == y:
        print('this your number')
        break
    else:
        print('this is not your number')
        y = int(input('try again '))
