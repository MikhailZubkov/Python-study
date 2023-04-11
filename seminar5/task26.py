# Задача 26:  Напишите программу, которая 
# на вход принимает два числа A и B, и 
# возводит число А в целую степень 
# B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def pow (number1, number2):
    if number2 == 1:
        return number1
    else:
        result = number1*pow(number1, number2-1)
        return result
number1 = int(input('enter number1'))
number2 = int(input('enter number2'))
    
print(pow(number1, number2))