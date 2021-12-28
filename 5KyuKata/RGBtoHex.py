def rgb(r, g, b):
    return ''.join((hex(max(0,min(255,x)))[2:].zfill(2)).upper() for x in [r,g,b])

print(rgb(-20,275,112))