#https://www.codewars.com/kata/52eb114b2d55f0e69800078d/train/python

class Cipher:
    def __init__(self, map1, map2):
        self.enc_key = str.maketrans(map1, map2)
        self.dec_key = str.maketrans(map2, map1)

    def encode(self, stg):
        return stg.translate(self.enc_key)

    def decode(self, stg):
        return stg.translate(self.dec_key)
