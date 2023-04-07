# Задача 18: Требуется найти в массиве A[1..N] самый 
#близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число 
#N – количество элементов в массиве. В последующих  строках 
#записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
from random import randint
import math
quantity = int(input('enter the number of numbers'))
list1 = []
for i in range (quantity):
    a = randint(-100, 100)
    list1.append(a)
print (list1)
etalon = int(input('enter desired number'))
mostNear = list1 [0]
for i in range (len(list1)):
    x = i
    if abs(mostNear - etalon) < abs(list1[x] - etalon):
        mostNear = mostNear
    else:
        mostNear = list1 [x]
print (mostNear)











    # print (list1[x], end = ' ')