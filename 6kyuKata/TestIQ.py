def iq_test(numbers):
    numbers = [int(n) for n in numbers.split()]
    odd = sum(1 for n in numbers if n%2)
    return list([numbers.index(x)+1 for x in numbers if x%2 == 0])[0] if odd > 1 \
                else list([numbers.index(x)+1 for x in numbers if x%2 == 1])[0]
def iq_equal_zeroXD(numbers):
    numbers = [int(n) % 2 == 0 for n in numbers.split()]
    return numbers.index(True) + 1 if numbers.count(False) > 1 else numbers.count(False)
print(iq_test('1 2 2'))
print(iq_equal_zeroXD('1 2 2'))