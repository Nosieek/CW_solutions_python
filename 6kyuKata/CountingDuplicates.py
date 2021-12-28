def duplicate_count(text):
    return sum(1 for letter in set(text.lower()) if text.lower().count(letter) > 1)


print(duplicate_count("abcdeaB"))
