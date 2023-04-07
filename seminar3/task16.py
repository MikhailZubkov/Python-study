#Задача 16: Требуется вычислить, сколько раз 
#встречается некоторое число X в массиве A[1..N]. 
#Пользователь в первой строке вводит натуральное 
#число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. 
#Последняя строка содержит число X

#*Пример:*
#5
#    1 2 3 4 5
#    3
#    -> 1
from random import randint
quantity = int(input('enter number of numbers'))
list1 = []
i = 1
while i <= quantity:
    a = randint (-100,100)
    list1.append(a)
    i += 1
# массив задан
desired_number = int(input('enter desired number'))
x = 0
for i in range (quantity):
    if list1 [i] == desired_number:
        x += 1

print (list1)
print (f'desired number occurs {x} times')
print (desired_number)