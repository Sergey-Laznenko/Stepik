'''
Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке,
и после первого введенного нуля выводит сумму полученных на вход чисел.
'''

n = int(input())

s = 0

while n != 0:
    s += n
    n = int(input())
print(s)