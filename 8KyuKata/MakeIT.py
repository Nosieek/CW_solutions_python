class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


def most_money(students):
    money = lambda student: student.fives * 5 + student.tens * 10 + student.twenties * 20
    if len(students) == 1: return students[0].name
    D = {money(student):student.name for student in students}
    return "all" if len(D) == 1 else D[max(D)]


phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 1)

print(most_money([cam, geoff, phil]))
#print(most_money([cam, geoff]))
#https://www.codewars.com/kata/528d36d7cc451cd7e4000339/train/python