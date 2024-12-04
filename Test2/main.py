# # 1
# # 2
#
# #
# # def func_a(value):
# #     total = 0
# #     if value >= 15:
# #         total = total + 20
# #     elif value >= 10:
# #         total = total + 10
# #     else:
# #         total = total + 1
# #     return total
# #
# #
# # def func_b(value):
# #     total = 0
# #     if value > 10:
# #         total = total + 10
# #
# #     if value <= 5:
# #         total = total + 5
# #     else:
# #         total = total + 2
# #     return total
# #
# #
# # print(func_a(5))
# # print(func_b(8))
# # print(func_a(15))
# # print(func_b(12))
# # ###
# # a = "4"
# # b = 3
#
#
# # result = a + b
# # print(result)
#
# # s = "*2*3*4x7"
# # n = 2
# #
# #
# # def mystery(s: str, n: int) -> bool:
# #     i = 0
# #     while i < len(s):
# #         if not s[i] == '*':
# #             return False
# #         i = i + n
# #     return True
# #
# #
# # print(mystery(s, n))
#
#
# # def mystery(s: str, n: int) -> bool:
# #     i = 0
# #     c = 0
# #     while i < len(s):
# #         if s[i].isdigit():
# #             c = c + 1
# #         i = i + 1
# #     return c == n
# #
# #
# # n = 3
# # s = "djknw45347kk"
# # print(mystery(s, n))
#
#
# def func(x, y):
#     if x > 100:
#         return True
#     elif x < 0 and y == 10:
#         return True
#     return False
#
#
# print(func(105, 100))
#
#
# def merge_name_marks(names, marks1, marks2):
#     """
#     merge_name_marks(['Rutwa', 'Dan', 'Romina'], \
#                          [50, 47, 43], [35, 40, 53])
#     ['Rutwa', 85, 'Dan', 87, 'Romina', 96]
#     merge_name_marks(['Peter', 'Randy'], [30, 22], [54, 84])
#     ['Peter', 84, 'Randy', 106]
#     merge_name_marks([], [], [])
#     []
#     """
#     result = []
#     for i in range(len(names)):
#         marks = marks1[i] + marks2[i]
#         result.append(names[i])
#         result.append(str(marks))
#     return result
#
#
# print(merge_name_marks(['Rutwa', 'Dan', 'Romina'],
#                        [50, 47, 43], [35, 40, 53])
#       )
#
# CURRENT_YEAR = 2023
#
#
# def calculate_age(birth_date: str) -> int:
#     """
#     You can assume birth_date has the format YYYY-MM-DD and
#     represents a valid year, month, and day, no later than
#     the end of CURRENT_YEAR.
#     Return the age of the person with the birth date
#     birth_date at the end of the year CURRENT_YEAR.
#
#     calculate_age('2010-05-15')
#     13
#     calculate_age('1995-10-20')
#     28
#     calculate_age('2023-01-01')
#     0
#     """
#     year = birth_date[0:4]  # "2010"
#     return CURRENT_YEAR - int(year)
#
#
# print(calculate_age('2010-05-15'))
d = {
    1: {2: 3, 4: 5},
    6: {7: 8}}
res1 = list(d.keys())[0]  ## 1
res2 = list(d.values())[1]  ## {7: 8}
res3 = list(res2.values())[0]  ## {7: 8}
print(res1)
print(res2)
print(res3)


# all_even: 2 4 6 8 10
def get_valid_sublists(L: list[list[int]], threshold: int) -> list[list[int]]:
    result = []
    for i in range(len(L)):
        valid = True
        for j in range(len(L[i])):
            if L[i][j] <= threshold:
                valid = False
                break
        if valid:
            result.append(L[i])
    return result


print(get_valid_sublists([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5))
# [[7, 8, 9]] -> L[0][2]
print(get_valid_sublists([[15, 20], [10, 11], [30, 40], [7, 17]], 10))
