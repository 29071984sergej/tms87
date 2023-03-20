#Дан список целых чисел.
#Создать новый список, каждый элемент которого равен исходному элементу умноженн
arr = [i for i in range(1, 10)]
print(arr)
new_arr =[]
for elemnt in arr:
    new_elemnt = elemnt * -2
    new_arr.append(new_elemnt)
print(new_arr)
