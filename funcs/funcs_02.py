#Написать программу для работы с матрицами:
#Создание
#Вывод
#Сумма всех элементов
#Нахождение максимального элемента
#Нахождение минимального элемента.
from random import randint
def create_func():
    a = int(input('enter size - '))
    my_matrix = [[randint(1, 10) for _ in range(a)] for _ in range(a)]
