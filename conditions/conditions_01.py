#Ввести предложение. Если число символов в предложении
# кратно 3 - добавить ! к концу строки. Вывести строку на экран в любом случае
my_str = input("enter str - ")
lan_my_str = len(my_str)
print(lan_my_str)
if (lan_my_str % 3) == 0:
    my_str = my_str + '!'
print(my_str)

