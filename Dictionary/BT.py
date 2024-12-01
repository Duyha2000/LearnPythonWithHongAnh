students = {'Alice': 85, 'Bob': 92, 'Charlie': 87, 'David': 78}

new_dict = {}

def get_score(item):
    return item[1]

# item{key , value} -> item[0] = key -  item[1]: value
# Sort desc value dict:
sorted_students = sorted(students.items(), key = get_score, reverse=True)
print(sorted_students)
# Map - diction

contacts = {'Alice': '123-456-789', 'Bob': '986-987-309', 'Charlie': '555-555-555'}
name = 'Bob'

print(f"Số điện thoại của bạn là {contacts[name]}")