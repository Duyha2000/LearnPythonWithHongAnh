
def selectionSort(arr):
    for i in range(len(arr) -1):
        min_position = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_position]:
                min_position = j
        arr[i], arr[min_position] = arr[min_position], arr[i]

arr = [98, 29, 44, 20]
selectionSort(arr)
print(arr)






