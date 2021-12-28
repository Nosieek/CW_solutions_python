def break_caesar(message):
    my_message = message.lower().split()
    for shift in range(26):
        count_in_words = 0

        for word_from_mm in my_message:
            # print(word_from_mm)
            breaked_word = ''.join(chr((ord(letter) - shift - 97) % 26 + 97)
                                   for letter in word_from_mm if not letter in ',.?!')

            if breaked_word in WORDS: # set of WORDS is in task on Codewars
                count_in_words += 1
        if count_in_words > len(my_message) // 2:
            return shift

print(break_caesar("Hello, world!"))