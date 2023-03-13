#Получить сумму кубов натуральных чисел от n до m, используя цикл for
n = 2
m = 10
result_sum = 0
for i in range(n,m):
    result_sum += i ** 3
print(result_sum)
