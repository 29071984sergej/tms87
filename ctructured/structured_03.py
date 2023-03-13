#Получить на ввод количество рублей и копеек и
#вывести в правильной форме, например, 3 рубля, 1 рубль 25 копеек, 3 копейки
rub = int(input("enter rubls - "))
rub = int(rub)
kop = int(input("enter kop - "))
if(rubls !=0) and (kop !=0):
    print(f"{rubls} rub.{kop} kop")
elif(rubls !=0) and (kop == 0):
    print(f"{rubls}rub.")
else:
    print(f"{kop} kop")