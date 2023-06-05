# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def degree(a, b):
    if b <= 0 or b == 1:
       return (a)
    if b != 1:
        return (a * degree(a, b - 1))

a = int(input("Введите число 'А': "))
b = int(input("Введите число 'B': "))
print(degree(a, b))

# def power(base, exp):
#     if (exp == 1):
#         return (base)
#     if (exp != 1):
#         return (base * power(base, exp - 1))
# base = int(input("Введите число: "))
# exp = int(input("Введите его степень: "))
# print("Результат возведения в степень равен:", power(base, exp))

# base = int(input("Введите число 'А': "))
# exp = int(input("Введите число 'B': "))
# print(power(base, exp))