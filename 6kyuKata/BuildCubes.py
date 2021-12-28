def find_nb(m):
    i = 1
    res = 0
    while res <= m:
        res += i ** 3
        if res == m: return i
        i += 1
    return -1

print(find_nb(40539911473216))
