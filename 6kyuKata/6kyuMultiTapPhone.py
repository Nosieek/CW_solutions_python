def presses(phrase):
    text = phrase.lower()
    result = 0
    for x in text:
        if x in list('1*#adgjmptw '):
            result += 1
        elif x in list('0behknqux'):
            result += 2
        elif x in list('cfilorvy'):
            result += 3
        elif x in list('234568sz'):
            result += 4
        else:
            result += 5

    return result
