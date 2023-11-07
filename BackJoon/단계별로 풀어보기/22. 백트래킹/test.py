original_list = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 3], [2, 4], [2, 5], [3, 1], [3, 2], [3, 4], [3, 5], [4, 1], [4, 2], [4, 3], [4, 5], [5, 1], [5, 2], [5, 3], [5, 4]]

unique_list = []

for item in original_list:
    item = set(item)
    if item not in unique_list:
        unique_list.append(item)

for item in unique_list:
    print(" ".join(map(str, item)))