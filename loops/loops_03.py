#Просуммировать неопределенное количество чисел,
#вводимых пользователем, суммировать до тех пор, пока пользователь не введёт слово «стоп»

result_sum = 0
while True:
    number = input("enter number - ")
    if number == 'stop':
        print("the end")
        break
    result_sum += int(number)
    print(f'result_sum = {result_sum}')


