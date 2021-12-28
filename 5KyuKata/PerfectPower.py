import math
def is_perfect_power(n):
    m = 2
    while m < n:
        if m ** round(math.log(n,m)) == n:
            return [m, round(math.log(n, m))]
        if math.log(n, m) < 2:
            break
        m += 1
    return None
print(is_perfect_power(81))