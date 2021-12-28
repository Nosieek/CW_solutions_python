def find_uniq(arr):
    s = set(arr)
    for x in s:
        if arr.count(x) == 1:
            return x
