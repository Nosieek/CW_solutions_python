def find_outlier(integers):
    res = [value % 2 != 0 for value in integers]
    return integers[res.index(True) if res.count(True) == 1 else res.index(False)]

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))