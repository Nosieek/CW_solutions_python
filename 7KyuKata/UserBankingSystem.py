class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, value):
        if self.balance < value: raise ValueError()
        self.balance -= value
        return f"{self.name} has {self.balance}."

    def add_cash(self, value):
        self.balance += value
        return f"{self.name} has {int(self.balance)}."

    def check(self, other_user, value):
        if not other_user.checking_account: raise ValueError()
        s1, s2 = other_user.withdraw(value), self.add_cash(value)[:-1]
        return "{} and {}".format(s2, s1)

    def __str__(self):
        return "User({}, {}, {})".format(self.name, self.balance, self.checking_account)


