import math

a = int(input('a '))
b = int(input('b '))
c = int(input('c '))

if a + b > c and b + c > a and a + c > b:
    print('triangle')
    while True:
        ang_ab = math.acos((c ** 2 - a ** 2 - b ** 2) / (-2 * a * b))
        print('ab=', math.degrees(ang_ab))
        ang_bc = math.acos((a ** 2 - b ** 2 - c ** 2) / (-2 * b * c))
        print('bc=', math.degrees(ang_bc))
        ang_ac = math.acos((b ** 2 - a ** 2 - c ** 2) / (-2 * a * c))
        print('ac=', math.degrees(ang_ac))
        break
else:
    print('not triangle')
