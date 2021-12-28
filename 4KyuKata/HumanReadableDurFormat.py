def format(unites, word):
    if unites == 1:
        return '%d %s' %(unites, word)
    return '%d %ss' %(unites, word)

def format_duration(seconds):
    if not seconds:
        return 'now'

    units = (
        (365 * 24 * 60 ** 2,'year'),
        (24 * 60 ** 2, 'day'),
        (60**2,'hour'),
        (60, 'minute'),
        (1, 'second')
    )

    result = []
    for unit in units:
        time, word = unit
        if seconds >= time:
            unites = int(seconds/time)
            result.append(format(unites,word))
            seconds -= unites * time
    return ' and'.join(', '.join(result).rsplit(',',1))

print(format_duration(334324233))