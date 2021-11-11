# Дано вещественное число X (|X|<1) и целое число N (>0)
# Найти значение выражения X - X**2/2 + X**3/3 - ... + (-1)**(N-1)*X**N/N
# Полученное число является приближенным значением функции ln в точке 1 + X

import math

x = input("Введите число x: ")
while type(x) != float:                  # обработка исключений
    try:
        x = float(x)
    except ValueError:
        print("Введите снова!")
        x = input("Введите вещественное число: ")
while abs(x) >= 1:                      # обработка исключений
    x = input("Введите число меньше единицы по модулю: ")
    while type(x) != float:
        try:
            x = float(x)
        except ValueError:
            print("Введите снова!")
            x = input("Введите вещественное число: ")

n = input("Введите целое число n: ")
while type(n) != int:                  # обработка исключений
    try:
        n = int(n)
    except ValueError:
        print("Введите снова!")
        n = input("Введите целое число: ")
while n <= 0:                          # обработка исключений
    n = input("Введите положительное число: ")
    while type(n) != int:
        try:
            n = int(n)
        except ValueError:
            print("Введите снова!")
            n = input("Введите целое число: ")

num1 = 1
res = 0
while num1 < int(n):
    num2 = (-1) ** (num1 - 1)
    num3 = abs(x) ** num1 / num1
    num4 = num2 * num3
    res += num4
    num1 += 1
print("Значение выражения равно: ", res)
print("Приближенное значение функции ln в точке (1+x) равно: ", math.log(1 + abs(x)))
