def dont_give_me_five(start,end):
    return sum('5' not in str(i) for i in range(start, end + 1))

print(dont_give_me_five(4,17)) # output [4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17] always without 5 in value
print(dont_give_me_five(1,6)) # output[1, 2, 3, 4, 6]
