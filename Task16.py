# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
# 1 2 3 4 5
# 3
# -> 1
n = int(input("Введите кол-во элементов массива: "))
a = [int(i) for i in input("Введите числа: ").split()]
if n != len(a):
    print("Вы ввели неверное кол-во элементов")
else:
    x = int(input("Введите число которое нужно вычислить: "))
    count = 0
    for i in range(len(a)):
        if a[i] == x:
            count += 1
    print(count)

n = int(input("Введите кол-во элементов: "))
array = [int(i) for i in input("Введите значения массива: ").split()] 
x = int(input("Введите число, которое нужно подсчитать: "))
count = 0
for el in array:
    if el == x:
        count += 1
print(count)