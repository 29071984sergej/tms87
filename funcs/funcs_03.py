#Написать программу для нахождения факториала.
#Факториал натурального числа n определяется как произведение
# всех натуральных чисел от 1 до n включительно
n = int(input())
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)
def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n
print(fac(5))