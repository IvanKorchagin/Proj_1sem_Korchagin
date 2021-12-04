# Дан целочисленный список размера N.
# Если он содержит все числа от 1 до N, то вывести 0;
# в противном случае вывести номер первого недопустимого элемента.


import random
list1 = []
N = int(input("Введите количество элементов списка: "))
for i in range(N):                                      # Находим случайный список размера N
    list1.append(random.randint(1, N))
    list1.sort()
print("Получившийся случайный список: ", list1)


def check_arr(arr):                                    # Функция по нахождению одинаковых элеметов в массиве
    n = len(arr)
    res = []
    arr2 = set(arr)
    for u in range(n - 1):
        for j in range(u + 1, n):
            if arr[u] == arr[j]:
                res.append(j+1)
                print("Номер первого недопустимого элемента списка: ", end="")
                return res
            if len(arr) == len(arr2):
                print("Список содержит все числа от 1 до N: ", end="")
                return [0]


print(check_arr(list1))