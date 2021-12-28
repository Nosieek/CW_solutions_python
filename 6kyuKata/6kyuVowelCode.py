def encode(st):
    key = {
        'a': '1',
        'e': '2',
        'i': '3',
        'o': '4',
        'u': '5'
    }
    return ''.join(key[x] if x in key else x for x in st)
def decode(st):
    key = {
        '1': 'a',
        '2': 'e',
        '3': 'i',
        '4': 'o',
        '5': 'u'
    }
    return ''.join(key[x] if x in key else x for x in st)