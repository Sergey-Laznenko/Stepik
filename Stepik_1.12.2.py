"""
Напишите программу, принимающую на вход целое число, которая выводит True,
если переданное значение попадает в интервал (-15, 12] \cup (14, 17) \cup [19, +\infty)(−15,12]∪(14,17)∪[19,+∞) и False
в противном случае (регистр символов имеет значение).
"""

a = int(input())
if (-15 < a <= 12) or (14 < a < 17) or (19 <= a ):
    print('True')
else:
    print('False')