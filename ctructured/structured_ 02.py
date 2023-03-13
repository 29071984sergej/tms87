#Ввести строку с клавиатуры.
#Вернуть результат логического выражения: или длина строки не меньше 8 в строке есть “python”.
#string = input("print string - ")
#string = str(string)
my_str = input("enter str - ")
len_my_str = len(my_str)
result_bool = (len_my_str >=8) or ("python"in my_str)
print(f'результат или длина строки не меньше 8 в строке есть“python” == {result_bool}')
