"""
На вход программе подается строка генетического кода, состоящая из букв А (аденин), Г (гуанин), Ц (цитозин), Т (тимин).
Напишите программу, которая подсчитывает сколько аденина, гуанина, цитозина и тимина входит в данную строку генетического кода.
"""

text = input().lower()
a = text.count('а')
g = text.count('г')
c = text.count('ц')
t = text.count('т')
print(f'Аденин: {a}\nГуанин: {g}\nЦитозин: {c}\nТимин: {t}')