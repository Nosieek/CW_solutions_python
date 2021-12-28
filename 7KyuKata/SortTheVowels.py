def sort_vowels(s):
    try:
        return '\n'.join('|'+letter if letter in 'aeoiu' else letter + '|'for letter in s)
    except:
        return ''
