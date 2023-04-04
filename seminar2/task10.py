#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
#а некоторые – гербом. Определите минимальное 
#число монеток, которые нужно перевернуть, 
#чтобы все монетки были повернуты вверх одной и 
#той же стороной. Выведите минимальное количество монет, 
#которые нужно перевернуть
from random import randint
numberCoins = int(input('enter the number of coins:'))
orel = 0
reshka = 0
while numberCoins > 0:
    a = randint(0,1)
    print (a)
    if a == 0:
        orel += 1
    else:
        reshka += 1
    numberCoins -= 1
print()
if orel < reshka:
    print(f"min quantity of coins - {orel}")
else:
    print(f"min quantity of coins - {reshka}")
