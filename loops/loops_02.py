#Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10.
from random import randint
arr = [randint(-9, 9) for _ in range(9)]
arr_2 = []
for i in range(10):
    arr_2.append(randint(-9, 9))
print(arr_2)
#Выведите результат сложения всехчисел больше 10.
resault = 0
for i in arr:
    if i > 10:
        resault += 1
        print(resault)