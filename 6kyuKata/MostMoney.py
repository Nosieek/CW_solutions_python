'https://www.codewars.com/kata/528d36d7cc451cd7e4000339/train/python'
class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


def most_money(students):
    money = [student.fives * 5 + student.tens * 10 + student.twenties * 20 for student in students]
    if money.count(max(money)) > 1:
        return 'All'
    else:
        return students[money.index(max(money))].name

