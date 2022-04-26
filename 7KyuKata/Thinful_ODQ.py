class Quark(object):
    def __init__(self, color, flavor, baryon_number = 1.0 / 3):
        self.color = color
        self.flavor = flavor
        self.baryon_number = baryon_number


    def interact(self, other):
        self.color, other.color = other.color, self.color


q1 = Quark("red", "up")
q2 = Quark("blue", "strange")
print(q1.color)
q1.interact(q2)
print(q1.color, q2.bayron_number)