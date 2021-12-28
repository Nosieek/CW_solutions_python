from functools import reduce
def persistence(n):# conver zadania tip przeksztalc na str
    number = [int(x) for x in str(n)]
    count = 0

    while len(str(n)) > 1:
        new_number = reduce(lambda x, y: x * y, number)
        number = [int(x) for x in str(new_number)]
        if 
        count += 1
    return count
print(persistence(33))
