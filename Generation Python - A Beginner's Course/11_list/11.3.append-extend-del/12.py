"""
На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу,
которая создает из указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам,
а затем выводит полученный список.
"""

n = int(input())
data = []
for _ in range(n):
    num = int(input())
    data.append(num)
del data[1::2]
print(data)
