def find_it(seq):
    result = 0
    for x in seq:
        result = result ^ x
    return result