class Dictionary():
    def __init__(self):
        self.book = {}

    def newentry(self, word, definition):
        self.book[word] = definition

    def look(self, key):
        return self.book.get(key, "Can't find entry for {}".format(key))

d = Dictionary()
d.newentry("Ja", "to ja")
d.newentry("d", "huj")
print(d.look("Ja"))
print(d.look("d"))