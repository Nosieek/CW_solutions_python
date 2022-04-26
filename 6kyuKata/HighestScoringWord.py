def high(x):
    res = []
    for text in x.split(' '):
        res.append(sum(ord(x) - 96 for x in text))
    return x.split(' ')[res.index(max(res))]
