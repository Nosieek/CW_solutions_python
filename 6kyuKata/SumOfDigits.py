#first solution
def digital_root(n):
    value = str(n)

    while True:
        result = 0
        for number in value:
            result += int(number)

        if len(str(result)) < 2:
            break
        value = str(result)
    return result

#Second solution
def digital(n):
    return n if n <= 10 else digital(sum(map(int, str(n))))

print(digital(999999999999))
