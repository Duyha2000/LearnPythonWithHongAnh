def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        # vòng lặp cho mảng đã được sắp xếp
        j = i - 1 # so sánh với phần tử đầu tiên của mảng đã được sắp xếp
        while j >= 0  and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1 # (đẩy temp sang bên trái)
        # Chèn giá trị:
        arr[j+1] = temp
# dictionary -> dictionary
# String , dic, list, io file, regex, tuple

# String (regex)
arr = [94, 30, 14, 20, 444, 2091, 390, 29, 1]

arr.sort()
# # Backend: tư duy logic viết code
# # Frontend:
#
# arr2 = [1,3,5,7,4]
# #           2 3
# temp = 4
# # so sánh 4 với 7
# # [ 1 , 3 , 5 ,..., 7]
# # [ 1 , 3 , ... , 5, 7]
#
# # [ 1,3 ,... , 5 , 7 ]
# #         2    3   4
# # arr[j + 1] = temp
# insertionSort(arr)
print(arr)