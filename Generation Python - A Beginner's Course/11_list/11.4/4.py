"""
На вход программе подается натуральное число nn, а затем nn различных натуральных чисел. Напишите программу,
которая удаляет наименьшее и наибольшее значение из указанных чисел, а затем выводит оставшиеся числа каждое на отдельной строке,
не меняя их порядок.
"""

n = int(input())
data = []
for _ in range(n):
    num = int(input())
    data.append(num)
n1, n2 = max(data), min(data)
data.remove(n1)
data.remove(n2)
print(*data, sep='\n')
