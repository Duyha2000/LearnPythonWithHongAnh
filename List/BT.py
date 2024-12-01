# def count(xs: list[int],ys: list[int]) -> int:
#     count = 0
#     for x in xs:
#         for y in ys:
#             if x == y:
#                 count += 1
#     return count
#
# m = count([1,2],[1,2,3,4])
# print(m)
# n = count([1,2],[1,2,2,1, 2,3,4])
# print(n)

# xs = [2 3 4 5] -> 2 3 2 5 - > len = 4
#        x = 0 , 1 , 2 , [3]
# for i in range(0, 4)


# def make_unique(xs: list[int]) -> list[int]:
    # new_list = []
    # for x in xs:
    #     if x not in new_list:
    #         new_list.append(x)
    # return new_list

    #  for x + 1 -> index out of range
    #  x -> so sánh chính nó


# -> 1,2,2,2,3,1,4,-3
# [1 , 2, 3, 4, -3)
# m = make_unique([1,2,2,2,3,1,4,-3])
# print(m)

#def smallest(lst: list[int]) -> list[int]:
    #return [min(lst)]

#print(smallest([2,2,4,6,7,3]))

#1
names = ['Bob', 'Hans', "Zahara", 'Amitabha', "Dov", 'Maria']
print(names[2:5])
print(names[0:1])
print(names[3:6])

#2 l.remove(v)
lst = ["I am well."]
lst.insert(0,"How are you?")
print(lst)

#4
lst1 = [2,4,99,0,-3.,86.9, -101]
lst1.sort(reverse = True)
print(lst1)

#5:
# def every_third(lst: list) -> list:
#     result = []
#     for x in range(0, len(lst), 3):
#         result.append(lst[x])
#     return result
#
# print(every_third([1,2,3,4,5,6,7,8,9,10,11]))

def every_ith(L: list, i: int) -> list:
    result = []
    for i in range(0, len(L), i):
        result.append(L[i])
    return result

print(every_ith([1,2,3,4,5,6,7], 2))

def every_third_revisited(lst: list):
    return every_ith(lst,3)
print(every_third_revisited([1,2,3,4,5,6,7,8,9]))










