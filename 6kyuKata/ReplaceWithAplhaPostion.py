def alphabet_position(text):
    result = ''

    for letter in text.lower():
       # print(letter)
        if ord(letter) in range(96) :
            continue

        if result:
            result += ' '
        result += str(ord(letter)-96)

    return result

#Second solution

def alphabet_position2(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

print(alphabet_position2("35dsadas6"))
