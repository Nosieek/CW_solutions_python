def array_diff(a, b):
    return [value for value in a if not value in b]

print(array_diff([1,1,2,3,1,2,3,3], [1]))