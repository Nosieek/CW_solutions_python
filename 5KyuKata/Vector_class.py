class Vector:
    def __init__(self, list):
        self.list = list

    def __iter__(self):
        return iter(self.list)

    def check_length(f):
        def wrapper(self, object):
            if len(self.list) != len(object.list):
                raise ValueError()
            return f(self, object)
        return wrapper

    @check_length
    def add(self, object):
        return Vector([x + y for x,y in zip(self.list, object.list)])

    @check_length
    def subtract(self, object):
        return Vector([x - y for x, y in zip(self.list, object.list)])

    @check_length
    def dot(self, object):
        return sum([x * y for x, y in zip(self.list, object.list)])

    def norm(self):
        return sum([x ** 2 for x in self.list]) ** 0.5

    def __str__(self):
        return '({})'.format(",".join(map(str, self)))

    def equals(self, object):
        return self.list == object.list
