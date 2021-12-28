def expanded_form(num):
    stringens = ''
    out = ''
    for count, value in enumerate(str(num)[::-1]):
        if value != '0':
            stringens += ' + ' + count * '0' + value
    out += stringens.strip(' + ')
    return out[::-1]