#Дан двумерный массив n × m элементов.
#Определить, сколько раз встречается число 7 среди элементов массива.
from random import randint

n = int(input("enter number - "))
m = int(input("enter number - "))
arr = []
for i in range(n):
    arr_1 = []
    for j in range(n):
        arr_1.append(randint(4, 9))
    #print(arr_1)
    arr.append(arr_1)
print(arr)
count = 0
for arr_i in arr:
    for j in arr_1:
        if j == 7:
            count += 1
print(count)