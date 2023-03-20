#Есть список arr = [1,2,3,4,4,4,5,5,2]
#1. Найти сумму всех числел
#2. Найти среднее арифметическое
#3. Найти среднее геомнтрическое
#4. Найти массив квадратов
#5*. Найти кумулятивную сумму
#6*. Найти медиану
#7*. Найти верхнюю и нижнюю квартил
arr = [1,2,3,4,4,4,5,5,2]
resault = sum(arr)
print(resault)
#import statistics;
#listnumbers = [1,2,3,4,4,4,5,5,2];
#print("The mean is =",statistics.mein(listnumbers))
import statistics
g_mein = statistics.geometrik_mein([1,2,3,4,4,4,5,5,2])
round(g_mein,1)
print(g_mein)
#couunt = 0
#resault = 0
#while count < len(arr)
  #  resault += arr[count]
  #  count += 1
#print(resault)

#resault = 0
#while arr:
  #  resault <= arr.pop(0)
#print(resault)
# Найти верхнюю квартил - = 0,75*(n+1)
arr = [1,2,3,4,4,4,5,5,2]
arr.sort()
print(arr)
index_v_dkvar = 0,75*(len(arr)-1)
if index_v_dkvar % 1:
    print(arr[index_v_dkvar])
else:
    resault = (arr[int(index_v_dkvar)]+arr[int(index_v_dkvar)+1])/2

    print(resault)