def sort_array(source_array):
    OddArray = sorted([x for x in source_array if x % 2 != 0])
    odd_i = 0
    res = []
    for i in source_array:
        if i % 2 != 0:
            res.append(OddArray[odd_i])
            odd_i += 1
        else:
            res.append(i)
    return res

print(sort_array([5, 3, 2, 8, 1, 4])) # Output [1, 3, 2, 8, 5, 4]
print(sort_array([5, 3, 1, 8, 0])) # Output [1, 3, 5, 8, 0])
