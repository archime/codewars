"""
Title: Strip comments
Complete the solution so that it strips all text that follows any of a set of 
comment markers passed in. Any whitespace at the end of the line should also be
stripped out.
"""

import unittest

def solution(string, markers):
    lines = string.split('\n')
    for marker in markers:
        for idx, line in enumerate(lines):
            if marker in line:
                lines[idx] = line[:line.find(marker)].rstrip()
    return "\n".join(lines)

###################################
# Define tests

class TestFunctions(unittest.TestCase):
    
    def test(self):
        solution1 = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
        compare1 = "apples, pears\ngrapes\nbananas"
        self.assertEqual(solution1, compare1)
        self.assertEqual(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")

###################################
# Run tests

if __name__ == '__main__':
    unittest.main()
