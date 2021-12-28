def narcissistic( value ):
    return True if sum(int(u) ** int(len(str(value))) for u in str(value)) == value else False
    #Better option
    #return value == sum(int(u) ** int(len(str(value))) for u in str(value))


print(narcissistic(371))