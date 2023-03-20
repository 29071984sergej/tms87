#В заданной строке расположить в обратном порядке все слова.
#Разделителями слов считаются пробелы.
str = "welkome to python."
#reserved = ''
#length = len(str) - 1
#while length >= 0:
    #reserved = reserved  + str[length]
    #length = length - 1
#print(reserved)
str_list = list(str)
str_list.reverse()
reversed = ''.join(str_list)
print(reserved)