"""
На вход программе подается одно число nn. Напишите программу, которая выводит список,
состоящий из n букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.
"""

n = int(input())
b = []
for i in range(97, 97 + n):
    b += (chr(i))
print(b)
