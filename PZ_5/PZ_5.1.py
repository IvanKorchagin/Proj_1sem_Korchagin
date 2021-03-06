# Вариант 21
# Составить функцию, которая выполнит суммирования числового ряда (1 + 2 + ... + N).

def summa(n):                                                 # функция, находящая сумму числового ряда
    sum1 = 0
    res = 0
    print("Сумма членов числового ряда:", "( ", end="")
    while sum1 < n:
        sum1 += 1
        res += sum1
        print(sum1, end=" ")
    print(")", "=", res, end=" ")
    return res


N = input("Введите количество членов числового ряда: ")
while type(N) != int:                   # обработка исключений
    try:
        N = int(N)
    except ValueError:
        N = input("Введите целое положительное число: ")
summa(N)
