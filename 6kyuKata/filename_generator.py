'''https://www.codewars.com/kata/586a933fc66d187b6e00031a/train/python'''
import string
import random
def generateName():
    return ''.join(random.choice(string.ascii_letters) for x in range(6))
