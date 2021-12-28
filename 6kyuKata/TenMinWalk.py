def is_valid_walk(walk):
    #determine if walk is valid
    end_x, end_y = 0, 0
    x, y = 0, 0
    directX = {
        'w': -1,
        'e': 1
    }
    directY = {
        'n': 1,
        's': -1
    }
    for direct_walk in walk:
        if direct_walk in directX:
            x += directX[direct_walk]
        else:
            y += directY[direct_walk]
    return len(walk) == 10 and ((x, y) == (end_x, end_y))


print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))

# or second solution
def is_walk(walk):
    return len(walk) == 10 and (walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w'))

print(is_walk(['n','n','n','s','s','s','n','s','n','s']))
