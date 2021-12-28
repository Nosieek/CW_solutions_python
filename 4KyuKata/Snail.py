'''
    Given a matrix of m x n elements (m rows, n columns),
    return all elements of the matrix in spiral order.
    For example,
    Given the following matrix:
    [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
    It should return [1,2,3,6,9,8,7,4,5]

'''

def snail(snail_map):
    result = []
    if not len(snail_map): # if snail is epmty
        return result

    #initial variable
    row_begin, row_end = 0, len(snail_map) -1
    column_begin, column_end = 0, len(snail_map[0])-1

    while row_begin <= row_end and column_begin <= column_end:
        for move_right in range(column_begin, column_end+1): #hoing rihjh
            result.append(snail_map[row_begin][move_right])
        row_begin += 1

        for move_down in range(row_begin, row_end+1): #going to down
            result.append(snail_map[move_down][column_end])
        column_end -= 1

        if row_begin <= row_end:# if true we going left
            for move_left in range(column_end, column_begin-1,-1):
                result.append(snail_map[row_end][move_left])
            row_end -= 1

        if column_begin <= column_end: # going up
            for move_up in range(row_end, row_begin-1, -1):
                result.append(snail_map[move_up][column_begin])
            column_begin += 1
    return result

print(snail([[1,2,3],
             [4,5,6],
             [7,8,9],
             ]))

