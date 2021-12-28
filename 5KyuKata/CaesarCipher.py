from string import ascii_uppercase as letters
def moving_shift(s, shift):
    new_string = ''
    arr = []
    for x in s:

        if x.upper() not in letters:
            new_string += x
        else:
            if ord(x)>= 97:
                new_string += chr(((ord(x) + shift) - 97) % 26 + 97)
            else:
                new_string += chr(((ord(x) + shift) - 65) % 26 + 65)
        shift += 1

    if len(s)%5 == 0:
        length = len(s)//5
    else:
        length = len(s)//5 + 1

    for i in range(4):
        a = i * length
        b = a + length
        arr.append(new_string[a:b])
    arr.append(new_string[b:])
    return arr


def demoving_shift(s, shift):
    s = ''.join(s)
    new_s = ''
    for x in s:
        if x.upper() not in letters:
            new_s += x
        else:
            if ord(x)>= 97:
                new_s += chr(((ord(x) - shift) - 97) % 26 + 97)
            else:
                new_s += chr(((ord(x) - shift) - 65) % 26 + 65)
        shift += 1
    return new_s
