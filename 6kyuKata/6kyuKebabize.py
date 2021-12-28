import re
def kebabize(string):
    new_string = ''
    patern = r'[0-9]'
    string = re.sub(patern, '', string)
    for x in string:
        if x == x.upper():
            new_string += '-' + x.lower()
        else:
            new_string += x
    if len(new_string) > 0:
        return new_string if new_string[0] != '-' else new_string[1:]
    return ''