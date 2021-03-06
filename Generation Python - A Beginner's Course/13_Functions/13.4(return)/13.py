"""
На вход программе подается число nn, а затем nn строк, содержащих целые числа в порядке возрастания.
Из данных строк формируются списки чисел. Напишите программу, которая объединяет указанные списки в один
отсортированный список с помощью функции quick_merge(), а затем выводит его.

На вход программе подается натуральное число nn, а затем nn строк, содержащих целые числа в порядке возрастания,
разделенные символом пробела.
"""


def quick_merge():
    data = []
    for _ in range(n):
        numbers = [int(i) for i in input().split()]
        data += numbers
        data = sorted(data)
    return data


n = int(input())
print(*quick_merge())
