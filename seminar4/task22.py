#Задача 22: Даны два неупорядоченных набора целых 
#чисел (может быть, с повторениями). Выдать без 
#повторений в порядке возрастания все те числа, 
#которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. 
#n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

from random import randint

list1 = []
list2 = []

quantity1 = int(input('enter quantity of elements in first set'))
quantiny2 = int(input('enter quantity of elements in second set'))
#set arrays of elements
for i in range (quantity1):
    list1.append(int(input('enter 1st array element'))) #(randint(-100, 100))

for i in range (quantiny2):
    list2.append(int(input('enter 2nd array element'))) #(randint(-100,100))

# print(list1, list2, sep= '\n')
#set elements in ascending order
list1.sort()
list2.sort()
print(list1, list2, sep= '\n')

#convert list to set
set1 = set(list1)
set2 = set(list2)
# print(set1, set2, sep= '\n')

#finding common elements

common1 = set1.intersection(set2)
# print(common1)

list3 = list(common1)
list3.sort()
print(list3)