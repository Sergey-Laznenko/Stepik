"""
Требуется определить, является ли данный год високосным.
Программа должна корректно работать на числах 1900 ≤ n ≤ 3000.
Выведите "Високосный" в случае, если считанный год является високосным и "Обычный"
в обратном случае (не забывайте проверять регистр выводимых программой символов).
"""

# put your python code here
a = int(input())
if 1900 <= a <= 3000:
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print('Високосный')
    else:
        print('Обычный')
else:
    print('Введен неверный год')
