from collections import defaultdict
def dict(n):
    dec = defaultdict(lambda: 0)
    i = 2
    while n > 1:
        while n % i == 0:
            n /= i
            dec[i] += 1
        i += 1
    return dec
def decomp(n):
    result = defaultdict(lambda:0)
    for i in range(2, n+1):
        for key, value in dict(i).items():
            result[key] += value
    return ' * '.join('{}^{}'.format(x, y) if y > 1 else str(x) for x, y in sorted(result.items()))


print(decomp(12))