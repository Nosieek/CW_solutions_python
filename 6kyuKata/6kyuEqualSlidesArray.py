def find_even_index( arr ):
    for i in range(len(arr)):
        left_arr = arr[:i]
        right_arr = arr[i+1:]
        if sum(left_arr) == sum(right_arr):
            return i
    return -1
print(find_even_index([1,2,3,4,3,2,1])) # output 3
print(find_even_index([1,100,50,-51,1,1])) # output 1
print(find_even_index([1,2,3,4,5,6])) # output -1
print(find_even_index([20,10,30,10,10,15,35]))# output 3
print(find_even_index([20,10,-80,10,10,15,35]))# output 0
print(find_even_index([10,-80,10,10,15,35,20])) # output 6
print(find_even_index(list(range(1,100))))# output -1
print(find_even_index([0,0,0,0,0]))# output Should pick the first index if more cases are valid
print(find_even_index([-1,-2,-3,-4,-3,-2,-1])) # output 3
print(find_even_index(list(range(-100,-1)))) # output-1