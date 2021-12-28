def get_sum(a,b):
    return sum(x for x in range(a,b+1)) if a < b else sum(x for x in range(b, a +1))

print(get_sum(-1, 2))
c = 4
d = 5
for x in range(c, d):
    print(x)