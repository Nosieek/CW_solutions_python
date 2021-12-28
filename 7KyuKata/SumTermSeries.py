def series_sum(n):
    return '{:.2f}'.format(sum(1/(1+x*3) for x in range(n)))
