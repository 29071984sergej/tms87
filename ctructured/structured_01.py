#Ввести число с клавиатуры.
# Вернуть результат логического выражения: число больше 15 и число кратно 5.
my_number = input("enter number - ")
my_number = int(my_number)
result = (my_number > 15 and not(my_number % 5))
result = (my_number > 15) and (my_number % 5) == 0
print(my_number > 15 and not(my_number % 5))
print(result)