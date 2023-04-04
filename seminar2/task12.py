#Петя и Катя – брат и сестра. Петя – студент, 
#а Катя – школьница. Петя помогает Кате по математике. 
#Он задумывает два натуральных числа X и Y (X,Y≤1000), 
#а Катя должна их отгадать. Для этого Петя делает две 
#подсказки. Он называет сумму этих чисел S и их 
#произведение P. Помогите Кате отгадать задуманные Петей числа.
summa = int(input('Enter the Sum of numbers'))
proizvedenie = int(input('enter the product of numbers'))
x = 0
y = 0
while y != summa - x and x < summa:
    x += 1
    if proizvedenie % x == 0:
        y = int (proizvedenie/x)
        if y == summa - x:
            print (f'Это {x} и {y}')
if y != summa - x or proizvedenie > summa:
    print('нет решения')