"""
Дано натуральное число n, (n ≥ 10). Напишите программу, которая определяет его максимальную и минимальную цифры.
"""

num = int(input())
b = ''
while num != 0:
    last = num % 10
    b += str(last)
    num = num // 10
print(f'Максимальная цифра равна {max(str(b))}')
print(f'Минимальная цифра равна {min(str(b))}')