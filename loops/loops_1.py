arr = [8, 1, 2, 15, 3, 4, 4, 4, 5, 5, 2, 6]

for i in range(len(arr)):
     for j in range(i, len(arr)):
        if arr[1] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)