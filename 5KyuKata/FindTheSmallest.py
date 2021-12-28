def smallest(n):
    value = str(n)
    min_value, from_index, into_index = n, 0, 0
    for i in range(len(value)):
        moved = value[:i] + value[i+1:]
       # print(moved)
        for j in range(len(moved)+1):
            number = int(moved[:j] + value[i] + moved[j:])
            if number < min_value:
                min_value, from_index, into_index = number, i, j
    return [min_value, from_index, into_index]



import unittest

class FindSmallest(unittest.TestCase):
    def testfrom_kata(self):
        self.assertEqual(smallest(261235), [126235, 2, 0])
        self.assertEqual(smallest(209917), [29917, 0, 1])
        self.assertEqual(smallest(261235), [126235, 2, 0])
        self.assertEqual(smallest(285365), [238565, 3, 1])
        self.assertEqual(smallest(269045), [26945, 3, 0])
        self.assertEqual(smallest(296837), [239687, 4, 1])


if __name__ == '__main__':
    unittest.main()
