def spin_words(sentence):
    return ' '.join(word if not len(word)>= 5 else word[::-1] for word in sentence.split())

print(spin_words("Hell hello world"))