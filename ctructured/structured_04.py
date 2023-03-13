#Введите число. Если это число делиться на 1000 без остатка,
#то выведите на экран "millennium"
my_int = int(input("enter numbers - "))
 (ifmy_int % 1000) == 0:
    print("millennium")
else:
    print("NOT millennium")
