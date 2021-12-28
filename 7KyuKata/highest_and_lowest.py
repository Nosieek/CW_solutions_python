def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split()]
    return '%d %d' % (max(numbers), min(numbers))


print(high_and_low("3 -5 42 -1 0 0 -9 4 7 4 -4"))
