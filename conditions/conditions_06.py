#Ввести почтовый адрес. Проверить доменное имя. В случае если оно gmail.com,
# вывести на экран имя почтового ящика. Иначе вывести надпись “DOMAIN NAME is not supported’
my_email = input("enter emeil-")
my_list = my_email.split("g")
print(my_list[-1])
if"gmail.com" in my_list[-1]:
    print(my_list)
else:
    print("DOMAIN NAME is not supported")


