"""
Напишите программу, которая подключает модуль math и, используя значение числа π из этого модуля,
находит для переданного ей на стандартный ввод радиуса круга периметр этого круга и выводит его на стандартный вывод.
"""

import math
r = float(input())
p = 2 * math.pi * r
print(p)