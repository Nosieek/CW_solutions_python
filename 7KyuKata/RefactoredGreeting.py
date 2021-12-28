# TODO: This method needs to be called multiple times for the same person (my_name).
# It would be nice if we didnt have to always pass in my_name every time we needed to great someone.

class Person:
    def __init__(self, my_name):
        self.my_name = my_name

    def greet(self, our_name):
        return "Hello %s, my name is %s" % (our_name, self.my_name)

    def name(self, change = None):
        if change is None:
            return self.my_name
        return "Person's name could not be retrieved"

jill = Person("jill")
print(jill.greet("kate"))
print(jill.name "test")