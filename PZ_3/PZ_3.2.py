# Вариант 21
# Даны два числа. Вывести порядковый номер меньшего из них.

x = input("Введите первое число: ")
while type(x) != int:           # обработка исключений
    try:
        x = int(x)
    except ValueError:
        print("Введите снова!")
        x = input("Введите первое число: ")
y = input("Введите второе число: ")
while type(y) != int:           # обработка исключений
    try:
        y = int(y)
    except ValueError:
        print("Введите снова!")
        y = input("Введите второе число: ")
if x < y:                                          # операция по сравнению чисел
    print("Порядковый номер меньшего числа: ", 1)
else:
    print("Порядковый номер меньшего числа: ", 2)
print("Программа успешно завершена!")
