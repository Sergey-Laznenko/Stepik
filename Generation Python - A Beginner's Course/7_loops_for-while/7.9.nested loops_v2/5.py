"""
На вход программе подается натуральное число nn. Напишите программу, которая находит цифровой корень данного числа.
Цифровой корень числа nn получается следующим образом: если сложить все цифры этого числа,
затем все цифры найденной суммы и повторить этот процесс, то в результате будет получено однозначное число (цифра),
которое и называется цифровым корнем данного числа.
"""

n = int(input())
a = n % 10
b = n // 10
c = a + b
while c >= 10:
    a = c % 10
    b = c // 10
    c = a + b
print(c)
