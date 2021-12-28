def shorten_to_date(long_date):
    return long_date[:long_date.index(',')]


print(shorten_to_date("Monday February 2, 8pm"))