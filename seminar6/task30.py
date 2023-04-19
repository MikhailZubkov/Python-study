# Задача 30:  Заполните массив элементами
# арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести 
# с клавиатуры. Формула для получения n-го 
# члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

firstelement = int(input('enter first element'))
difference = int(input('enter difference'))
quantity = int(input('enter quantity of elements'))

list1 = [firstelement]
a = [list1.append(list1[-1] + difference) for i in range (quantity-1)]
print (list1)
