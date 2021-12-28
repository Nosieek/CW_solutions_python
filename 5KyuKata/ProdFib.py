def productFib(prod):
    a, b = 0, 1
    while a * b < prod:
        a,b = b, b+a
    return [a,b,prod == a*b]
#smarter
def productFib2(prod):
    res = lambda a, b: res(b,a+b) if prod > a *b else [a, b, prod == a *b]
    return res(0,1)

print(productFib(4895))
print(productFib2(4895))

