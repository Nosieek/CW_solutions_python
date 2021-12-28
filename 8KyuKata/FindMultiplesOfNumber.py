def find_multiples(integer, limit):
    return [x for x in range(integer,limit+1)[::integer]]

print(find_multiples(2,6))