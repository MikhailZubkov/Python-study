# Задача 32: Определить индексы элементов 
# массива (списка), значения которых 
# принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума 
#  и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

list1 = list(map(int,input('enter elements with space').split()))
lower = int(input('enter lower value'))
higher = int(input('enter higher value'))
list2 = []
for i in range (0, len(list1)):
    if list1[i] >= lower and list1[i] <= higher:
        list2.append(i)
print(list1)
print(list2)