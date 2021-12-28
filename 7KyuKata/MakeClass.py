def make_class(*args):
    class Myclass:
        def __init__(self, *value):
            self.__dict__ = {x:y for x,y in zip(args, value)}
    return Myclass