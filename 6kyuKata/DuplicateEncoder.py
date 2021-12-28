def duplicate_encode(word):
    return ''.join( '(' if word.lower().count(new_word) == 1 else ')' for new_word in word.lower())
    #for new in word.lower():
      #  if word.lower():


print(duplicate_encode('!H(gq iXunbxAtA U'))
print('((((()())(())()))')