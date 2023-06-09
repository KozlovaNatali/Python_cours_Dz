# Задача 28: Вводится десятичное число. 
# Реализовать алгоритм его перевода в двоичную систему счисления через рекурсию. 
# Нельзя использовать функцию bin()
# *Пример:*
#     10
#     *Вывод:*
#     1010

def algorithm(n):
    if n > 1:
        algorithm(n // 2)
    print (n % 2, end="")

n = int(input("Введите десятичное число: "))
print(algorithm(n))


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2 -> 4
def summa(a, b):
    if b == 0:
        return a
    return summa(a + 1, b - 1)
a = int(input("Введите число 'А': "))
b = int(input("Введите число 'B': "))
print (summa(a, b))