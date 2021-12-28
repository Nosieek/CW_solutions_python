from string import ascii_lowercase as AS

def is_pangram(s):
    return set(AS) - set(s.lower()) == set([])

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))