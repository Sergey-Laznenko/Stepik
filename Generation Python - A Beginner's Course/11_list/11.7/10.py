"""
На вход программе подается строка текста. Напишите программу, использующую списочное выражение,
которая выводит все цифровые символы данной строки.
"""

# 1
print(''.join([i for i in input() if ord(i) in range(48, 58)]))

# 2
print(''.join([i for i in input() if i.isdigit()]))
