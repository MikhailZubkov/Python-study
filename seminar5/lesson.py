# def fib (n):
#     if n in [1, 2]:
#         return 1
#     return fib (n-1) + fib (n-2)

# list1 = []
# b = int(input('enter fib number'))
# for i in range (1, b+1):
#     list1.append(fib(i))
# print (list1)
def quick_sort (array):
    if len(array) <= 1:
        return (array)
    else:
        pivot = array[0]
    less = [i for i in array [1:] if i <= pivot]
    greater = [i for i in array [1:] if i > pivot]
    return quick_sort (less) + [pivot] + quick_sort(greater)

print (quick_sort([14, 5, 9, 6, 3]))