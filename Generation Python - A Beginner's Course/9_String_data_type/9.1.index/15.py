"""
На вход программе подается натуральное число, записанное в десятичной системе счисления. Напишите программу,
которая переводит данное число в двоичную систему счисления.
"""

n = input()
num = int(n)
t = ''
while num != 0:
    b = num % 2
    t += str(b)
    num //= 2
t = t[::-1]
print(t)
