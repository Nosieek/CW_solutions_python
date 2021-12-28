def max_subarray_sum(array): #function return maximum sum of subarray
    negative_count = len(list(filter(lambda x: (x < 0), array)))
    if not array or negative_count == len(array): # if our list is empty and we are having negative count
        return 0 # equal length of list we are returning 0

    max_till_now = array[0]
    max_ending = 0

    for number in array:
        max_ending += number
        if max_ending < 0:
            max_ending = 0

        elif max_till_now < max_ending:
            max_till_now = max_ending

    return max_till_now

import unittest

class MyTestOfSubarray(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(max_subarray_sum([]),0)

    def test_positive(self):
        self.assertEqual(max_subarray_sum([1000, 100, 69]), 1169)

    def test_negative_and_positive(self):
        self.assertEqual(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_subarray_sum([-10, 1,-1, 1000, 3,-99,4, -999, 2, -1, -5, 499, 1, 43, 63]), 1003)

if __name__ == '__main__':
    unittest.main()