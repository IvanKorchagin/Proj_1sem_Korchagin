# Дано множество A из N точек на плоскости и точка B (точки заданы своими
# координатами х, у). Найти точку из множества A, наиболее близкую к точке B.
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
# R = √((x2 – x1)^2 + (у2 – y1)^2).
# Для хранения данных о каждом наборе точек следует использовать по два списка: первый
# список для хранения абсцисс, второй — для хранения ординат.

import random
import math

abc = []
ordinate = []
N = int(input("Введите количество точек в множестве А: "))
for i in range(N):                                          # Находим случайный список размера N
    abc.append(random.randint(1, N))
    ordinate.append(random.randint(1, N))
    abc.sort()
    ordinate.sort()
print("Список абцисс: ", abc)
print("Список ординат: ", ordinate)

Bx = input("Введите координаты Bx: ")
By = input("Введите координаты By: ")
print("Точка B имеет координаты: ", "(", Bx, ";", By, ")")

i = 0
check = math.sqrt((int(abc[0]) - int(Bx)) ** 2 + ((int(ordinate[0]) - int(By)) ** 2))
Ax = abc[0]
Ay = ordinate[0]
while i < N:                                     # Находим ближайшую точку к точке B
    R = math.sqrt((int(abc[i]) - int(Bx)) ** 2 + ((int(ordinate[i]) - int(By)) ** 2))
    if R <= check:
        check = R
        Ax = abc[i]
        Ay = ordinate[i]
    i += 1
print("Ближайшая к точке B точка A имеет координаты: ", "(", Ax, ";", Ay, ")")
print("Расстояние между точками: ", check)
