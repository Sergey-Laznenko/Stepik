"""
На вход программе подается одна строка состоящая из цифр. Напишите программу, которая считает сумму цифр данной строки.
"""

a = input()
summa = 0
for i in a:
    summa += int(i)
print(summa)
