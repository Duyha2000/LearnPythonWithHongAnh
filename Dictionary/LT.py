# dict = {'key': 'value'}
my_dict = {'name':'Hung','age':24,'city':'HCM'}
# Tạo dictionary bằng hàm dict()
dict2=dict(name='Hung',age=24,city='HCM')
# Truy cập phần tử trong Dictionary
print(my_dict['name'])
# print(my_dict['key'])
# Phương thức clear() xóa tất cả các phần tử khỏi dictionary.
# my_dict.clear()
# print(my_dict)

# Phương thức copy() trả về một bản sao của dictionary.
dict3 = dict2.copy()
print(dict3)

# Phương thức get():
print(dict3.get('name'))
print(dict3.get('key')) # None

# Phương thức items():
print(dict3.items())

# lấy ra tất cả key trong dict:
print(dict3.keys())
# lấy ra tất cả value trong dict:
print(dict3.values())
# Phương thức update(): cập nhật tên là Trang
dict3['name'] = 'Trang'
dict3['tel'] = '+8482748'
# dict3.update({'tel':'+9292929'})
print(dict3)
# Duyệt qua các phần tử trong Dictionary:
# for k, v in dict3.items():
#     print(k,v)

# Xoá phần tử trong Dictionary: clear, del xóa luôn cặp key - value, pop()
# del dict3['tel']
# print(dict3)
#
# dict4 = dict3.pop('name')
# # print(dict4)
# print(dict3)

nested_dict = {
    'person1': {'name': 'John', 'age': 25},
    'person2': {'name': 'Jane', 'age': 30}
}
# Xóa đi age:
for values in nested_dict.values():
    del values['age']
print(nested_dict)