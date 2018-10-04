"""
Write a function called sum_intervals() that accepts an array of intervals,
and returns the sum of all the interval lengths. Overlapping intervals should
only be counted once.
"""

import unittest

def sum_intervals(array):
    # Sort array by first element of each interval
    array.sort()
    # Copy array, replacing tuples with lists
    array = [[interval[0], interval[1]] for interval in array]
    # Initialize important working variables
    interval_sum = 0
    curr_interval = []

    for idx, interval in enumerate(array):
        if idx == 0 or curr_interval == []:
            curr_interval = interval
        elif curr_interval[1] > interval[0]:
            curr_interval[1] = max(curr_interval[1], interval[1])
        else:
            interval_sum += curr_interval[1] - curr_interval[0]
            curr_interval = interval
        if idx == len(array) - 1 and curr_interval != []:
            interval_sum += curr_interval[1] - curr_interval[0]
            curr_interval = []
    return interval_sum

######################################################################
# Code for testing

class TestFunctions(unittest.TestCase):
    
    def setUp(self):
        self.interval1 = [[1,2], [6, 10], [11, 15]]
        self.interval2 = [[1,4], [7, 10], [3, 5]]
        self.interval3 = [[1,5], [10, 20], [1, 6], [16, 19], [5, 11]]
        self.interval4 = [[1, 2], [3, 10], [4, 5], [9, 11]]

    def tearDown(self):
        del self.interval1
        del self.interval2
        del self.interval3
        del self.interval4

    def test_sum_intervals(self):
        self.assertEqual(sum_intervals(self.interval1), 9, "Error: Interval 1")
        self.assertEqual(sum_intervals(self.interval2), 7, "Error: Interval 2")
        self.assertEqual(sum_intervals(self.interval3), 19, "Error: Interval 3")
        self.assertEqual(sum_intervals(self.interval4), 9, "Error: Interval 4")

######################################################################
# Run tests

if __name__ == '__main__':
    unittest.main()

