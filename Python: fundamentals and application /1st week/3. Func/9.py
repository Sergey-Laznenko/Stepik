"""
Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и возвращающую самое маленькое целое число y, такое что:

y больше или равно x
y делится нацело на 5
"""


def closest_mod_5(x):
    return (x + 4) // 5 * 5
