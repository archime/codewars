"""
Title: Snail sort
Given an n x n array, return the array elements arranged from outermost 
elements to the middle element, traveling clockwise.
Note: Could refactor using zip()!
"""

import unittest

def snail(array):
    array_copy = [row.copy() for row in array]
    output_list = []
    curr_dir = 0
    while len(array_copy) != 0:
        if curr_dir == 0:
            output_list.extend(array_copy.pop(0))
            curr_dir += 1
        elif curr_dir == 1:
            for row_num in range(len(array_copy)):
                last_element = array_copy[row_num][-1]
                array_copy[row_num] = list(array_copy[row_num][:-1])
                output_list.append(last_element)
            curr_dir += 1
        elif curr_dir == 2:
            bottom_row = array_copy.pop()
            bottom_row.reverse()
            output_list.extend(bottom_row)
            curr_dir += 1
        else:
            for row_num in reversed(range(len(array_copy))):
                first_element = array_copy[row_num][0]
                array_copy[row_num] = list(array_copy[row_num][1:])
                output_list.append(first_element)
            curr_dir = 0
    return output_list

###################################
# Define tests

class TestFunctions(unittest.TestCase):

    def test(self):
        array1 = [[1,2,3], [4,5,6], [7,8,9]]
        expected1 = [1,2,3,6,9,8,7,4,5]
        self.assertEqual(snail(array1), expected1)
        array2 = [[ 1, 2, 3, 4], [12,13,14, 5], [11,16,15, 6], [10, 9, 8, 7]]
        expected2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(snail(array2), expected2)

###################################
# Run tests

if __name__ == '__main__':
    unittest.main()
