class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, arg):
        if arg not in self.cache:
            self.cache[arg] = self.func(arg)
        return self.cache[arg]

@Memoize
def exp_sum2(n):
    if n == 0:
        return 1
    result, k, sign = 0, 1, 1
    while True:
        pent = (3*k**2 - k) // 2
        if pent > n:
            break

        result += sign * exp_sum2(n - pent)
        pent += k

        if pent > n:
            break

        result += sign * exp_sum2(n - pent)
        k += 1
        sign = -sign
    return result

print(exp_sum2(1))



