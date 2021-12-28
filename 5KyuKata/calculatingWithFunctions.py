def zero(function = None): return 0 if not function else function(0)
def one(function = None): return 1 if not function else function(1)
def two(function = None): return 2 if not function else function(2)
def three(function = None): return 3 if not function else function(3)
def four(function = None): return 4 if not function else function(4)
def five(function = None): return 5 if not function else function(5)
def six(function = None): return 6 if not function else function(6)
def seven(function = None):return 7 if not function else function(7)
def eight(function = None): return 8 if not function else function(8)
def nine(function = None): return 9 if not function else function(9)

def plus(y):return lambda x: x + y
def minus(y):return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: x // y

print(four(divided_by(five())))