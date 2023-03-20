#Создать квадратную матрицу размерностью n
#и заполнить ее случайными значениями. Найти сумму всех элементов матрицы, которые кратны 3.

result_sum = 0
for arr_i in arr:from random import randint

n = int(input("enter number - "))
arr = []
for i in range(n):
    arr_1 = []
    for j in range(n):
        arr_1.append(randint(4, 9))
    #print(arr_1)
    arr.append(arr_1)
#print(arr)
result_sum = 0
for arr_i in arr:
    print(arr_i)
    for i in arr_i:
        result_sum += i
    print(arr_i)  print(
    for i in arr_i:
      i)
        if(i % 3) == 0:
            result_sum = 0
        for arr_i in arr:
            print(arr_i)
        for i in arr_i:
            result_sum += i
print(result_sum)