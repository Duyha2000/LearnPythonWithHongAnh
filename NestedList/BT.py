#     """Insert v into lst just before the right most item greater than v, or at
#     index 0 if no items are greater than v.
#
#     >>> my_list = [3, 10, 4, 2]
#     >>> insert(my_list, 5)
#     >>> my_list:  [3, 5, 10, 4, 2]

#     >>> my_list = [5, 4, 2, 10]
#     >>> insert(my_list, 20)
#     >>> my_list
#     [20, 5, 4, 2, 10]
#     """

# v = 5
# 3 10 4 2

# 5 3 5 5 10 4 2
# def insert(lst: list[int], v: int) -> None:
#     for i in range(len(lst)-1):
#         if lst[i] > v:
#             lst.insert(i, v)
#             return
#     lst.insert(0, v)
#
# my_list = [3, 10, 4, 2]
# insert(my_list, 5)
# print(my_list)


book_series = {
    'Animorphs':
        {'author': 'K.A. Applegate', 'number': 54, 'genre': 'middle grade'},
    'Inheritance Games':
        {'author': 'Jennifer Lynn Barnes', 'number': 2, 'genre': 'adult'},
    'Shopaholic':
        {'author': 'Sophie Kinsella', 'number': 10, 'genre': 'adult'},
    'Everworld':
        {'author': 'K.A. Applegate', 'number': 12, 'genre': 'young adult'}
}


# # Tạo một dictionary
# my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
#
# # Lặp qua các cặp key-value
# for key, value in my_dict.items():
#     print(f"Key: {key}, Value: {value}")
# authors = []
# for details in book_series.values():
#     authors.append(details['author'])
# print(authors)
def convert_book_series_dict(book_series: dict[str, dict]) \
        -> dict[str, list[dict]]:
    # Initialize an empty dictionary for authors
    authors = []
    numbers = []
    genre = []
    series = []
    author_series = {}
    for serie, details in book_series.items():
        authors.append(details['author'])
    # Lấy tên tác giả từ thông tin của bộ sách:
        numbers.append(details['number'])
        genre.append(details['genre'])
        series.append(serie)


    for i in range(len(authors)):
        author = authors[i]
        if author not in author_series:
            author_series[author] = []
        author_series[author].append({'series': series[i], 'number': numbers[i],
                                      'genre': genre[i]})

    return author_series
print(convert_book_series_dict(book_series))
    # Nếu tác giả chưa tồn tại trong từ điển, thêm tác giả với danh sách rỗng
    # Thêm thông tin bộ sách vào danh sách của tác giả





