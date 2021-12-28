def unique_in_order(iterable):
    arr = []
    last = None
    for var in iterable:
        if var != last:
            arr.append(var)
        last = var
    return arr

print(unique_in_order([1,2,3,3,3,4,1,2]))