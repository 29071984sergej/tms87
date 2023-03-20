#Создать список с фамилиями. Вывести все фамилии,
#которые начинаются на П и заканчиваются на а
arr = ['Britva', 'Tyrecki','Pevcaya']
for vamilian in arr:
    if vamilian[0] == "P" and vamilian[-1] == 'a':
        print(vamilian)