# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


element1 = int(input("Введите 1 элемент массива: "))
difference = int(input("Введите разность: "))
length = int(input("Введите кол-во элементов массива: "))
for i in range(length):
    print(element1 + i * difference, end=' ')