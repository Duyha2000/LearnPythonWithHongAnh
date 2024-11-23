def bubbleSort(arr):
    for i in range(len(arr) -1):
        for j in range( 0, len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [94,30 ,14, 20, 444, 2091,390 , 29 ,1]

bubbleSort(arr)
print(arr)
