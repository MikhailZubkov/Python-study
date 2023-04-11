# Задача 28: Напишите рекурсивную функцию 
# sum(a, b), возвращающую сумму двух целых 
# неотрицательных чисел. Из всех 
# арифметических операций допускаются 
# только +1 и -1. Также нельзя использовать 
# циклы.
# *Пример:*
# 2 2
#     4 
flag = True
while flag:
    a = input("Введите число (A>=0): ")
    try:
        a = int(a)
        if a < 0:
            print('-> ОШИБКА: Введено отрицательное число!')
        else:
            flag = False
    except ValueError:
        print('-> ОШИБКА: Введено некорректное значение!')

flag = True
while flag:
    b = input("Введите число (B>=0): ")
    try:
        b = int(b)
        if b < 0:
            print('-> ОШИБКА: Введено отрицательное число!')
        else:
            flag = False
    except ValueError:
        print('-> ОШИБКА: Введено некорректное значение!')

def summ(a, b):
    if b == 0:
        return a
    return summ(a,b - 1) + 1

print(f'{a} + {b} = {summ(a, b)}')