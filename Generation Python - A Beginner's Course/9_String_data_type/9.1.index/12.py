"""
На вход программе подается одна строка. Напишите программу,
которая определяет сколько раз в строке встречаются символы + и *.
"""

a = input()
plus = 0
star = 0
for i in a:
    if i in '+':
        plus += 1
    if i in '*':
        star += 1
print(f'Символ + встречается {plus} раз')
print(f'Символ * встречается {star} раз')