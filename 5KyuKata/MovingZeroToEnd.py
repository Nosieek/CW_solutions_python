#from functools import reduce
def move_zeros(array):
    length_array = len(array)
    array = list(filter(None, array))
    array.extend([0] * (length_array - len(array)))
    return array

print(move_zeros([1, 0, 1,1]))