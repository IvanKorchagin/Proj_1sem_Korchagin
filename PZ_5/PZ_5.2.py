# Вариант 21
# Описать функцию Power1(A,B) вещественного типа, находящую величину А ^ В по формуле
# А ^ В = ехр(В*ln(А)) (параметры А и В — вещественные).
# В случае нулевого или отрицательного параметра А функция возвращает 0.
# С помощью этой функции найти степени А ^ P, В ^ Р, С ^ Р, если даны числа Р, А, В, С.

import math


def power1(x, y):                              # функция, находящая степень числа
    if float(x) > 0:
        res = round(math.exp(float(y) * math.log(x)), 10)
        return res
    else:
        return 0


P = input("Введите число P (степень чисел): ")
while type(P) != float:         # обработка исключений
    try:
        P = float(P)
    except ValueError:
        print("Введите снова!")
        P = input("Введите степень числа: ")
A = input("Введите число A: ")
while type(A) != float:         # обработка исключений
    try:
        A = float(A)
    except ValueError:
        print("Введите снова!")
        A = input("Введите число: ")
B = input("Введите число B: ")
while type(B) != float:         # обработка исключений
    try:
        B = float(B)
    except ValueError:
        print("Введите снова!")
        B = input("Введите число: ")
C = input("Введите число C: ")
while type(C) != float:         # обработка исключений
    try:
        C = float(C)
    except ValueError:
        print("Введите снова!")
        C = input("Введите число: ")
print("A ^ P = ", power1(A, P))
print("B ^ P =", power1(B, P))
print("C ^ P =", power1(C, P))
