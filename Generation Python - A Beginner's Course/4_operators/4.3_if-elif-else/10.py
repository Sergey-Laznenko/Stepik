"""
На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены цвета карманов:
-карман 0 зеленый;
- для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
- для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный;
- для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
- для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный.
Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным или черным.
Программа должна вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона от 0 до 36.
"""

x = int(input())

if x == 0:
    print('зеленый')
elif 1 <= x <= 10:
    if x % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 11 <= x <= 18:
    if x % 2 == 0:
        print('красный')
    else:
        print('черный')
elif 19 <= x <= 28:
    if x % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 29 <= x <= 36:
    if x % 2 == 0:
        print('красный')
    else:
        print('черный')
else:
    print('ошибка ввода')


# 2 вариант

a = int(input())
if 0 <= a < 37:
    if (0 < a < 11 or 18 < a < 29) and a % 2 or (10 < a < 19 or 28 < a < 37) and a % 2 == 0:
        print('красный')
    elif a == 0:
        print('зеленый')
    else:
        print('черный')
else:
    print('ошибка ввода')
