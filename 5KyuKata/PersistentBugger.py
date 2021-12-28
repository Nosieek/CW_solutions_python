def persistence(n):
    count = 0
    while n > 9:
        count += 1
        bufor = 1
        for nums in str(n):
            bufor *= int(nums)
        n = bufor
    return count

import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i

print(persistence(999))