def dig_pow(n, p):
    num = (int(x) for x in str(n))
    result = 0
    for i in num:
        result += i ** p
        p += 1
    if result % n:
        return -1
    return result // n