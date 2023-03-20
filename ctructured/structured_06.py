#Ввести строку. Если длина строки больше 10 символов,
#то создать новую строку с 3 восклицательными знаками в конце  ('!!!') и вывести на экран.
#Если меньше 10, то вывести на экран второй символ строки
my_str = input("enter str - ")
lan_my_str = len(my_str)
print(lan_my_str)
if (lan_my_str > 10):
    my_str = my_str + '!,!,!'
    print(my_str)
elif(lan_my_str < 10):

    print(my_str[1])