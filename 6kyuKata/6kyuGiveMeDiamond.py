def first_half(start, finish, step,all):
    return [(" " * int((all - x)/2)) + "*" * x + "\n" for x in range(start, finish, step)]

def second_half(start, finish, step,all):
    return [(" " * int((all - x)/2)) + "*" * x + "\n" for x in range(start, finish, step)]

def diamond(n):
    if (n % 2) == 0 or n < 0:
        return None
    expected = ''.join(first_half(1, n, 2,n))
    expected += ''.join(second_half(n, 0, -2,n))
    return expected

print(diamond(5))