"""
Прогуливаясь по Манхэттену, вы не можете попасть из точки А в точку Б по кратчайшему пути. Если только вы не умеете проходить сквозь стены,
вам обязательно придется идти вдоль его параллельно-перпендикулярных улиц.
"""

a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(abs(a - c) + abs(b - d))