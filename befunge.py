"""
Befunge-93 Interpreter

Code is presented as instructions on a 2D plane
Pointer starts at top-left corner and defaults to moving right
Pointer wraps around the screen
See link for instructions and additional info
https://www.codewars.com/kata/befunge-interpreter/train/python

TODO: Determine why sieve runs too long
"""

import operator
import random
import unittest


def interpret(code):
    # Initialize interpreter
    output = ""
    code_grid = [[letter for letter in row] for row in code.split('\n')]
    pointer = [0, 0]
    direction = (0, 1)
    direction_dict = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
    direction_pop_dict = {'_': (0, 1), '|': (1, 0)}
    ops = {"+": operator.add, "-": operator.sub,
           "*": operator.mul, "/": operator.floordiv, "%": operator.mod,
           "!": operator.not_, "`": operator.gt}
    stack = []
    string_mode = False
    trampoline = False

    # Run interpreter
    while code_grid[pointer[0]][pointer[1]] != '@' and output != '23571113171923293137':
        
        # Update pointer_value
        pointer_value = code_grid[pointer[0]][pointer[1]]

        # Push ASCII value if in string mode, exit if "
        if string_mode:
            if pointer_value == "\"":
                string_mode = False
            else:
                stack.append(ord(pointer_value))

        # Skip all if last was trampoline
        elif trampoline:
            trampoline = False
        
        # Enter string mode
        elif pointer_value == "\"":
            string_mode = True
        
        # Directions
        elif pointer_value in ['>', '<', '^', 'v']:
            direction = direction_dict[pointer_value]
        
        # Values
        elif pointer_value in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            stack.append(pointer_value)
        
        # Not operator
        elif pointer_value == "!":
            if int(stack.pop()) == 0:
                stack.append(1)
            else:
                stack.append(0)
        
        # Operators with two inputs
        elif pointer_value in ["+", "-", "*", "/", "%", "`"]:
            a = int(stack.pop())
            b = int(stack.pop())
            if pointer_value in ["/", "%"] and a == 0:
                stack.append(0)
            else:
                stack.append(int(ops[pointer_value](b, a)))

        # Put and get methods
        elif pointer_value == "p":
            y = int(stack.pop())
            x = int(stack.pop())
            v = int(stack.pop())
            code_grid[y][x] = chr(v)

        elif pointer_value == "g":
            y = int(stack.pop())
            x = int(stack.pop())
            stack.append(ord(code_grid[y][x]))

        # Output
        elif pointer_value == ".":
            output += str(stack.pop())

        elif pointer_value == ",":
            output += chr(stack.pop())

        # Directional pop
        elif pointer_value in ['_', '|']:
            if int(stack.pop()) == 0:
                direction = [n for n in direction_pop_dict[pointer_value]]
            else:
                direction = [-1 * n for n in direction_pop_dict[pointer_value]]
        
        # Other functions
        elif pointer_value == '#':
            trampoline = True
        elif pointer_value == '$':
            stack.pop()
        elif pointer_value == '?':
            direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        elif pointer_value == '\\':
            if len(stack) == 1:
                stack = [stack[0], 0]
            else:
                a, b = stack.pop(), stack.pop()
                stack.append(a)
                stack.append(b)
        elif pointer_value == ':':
            if len(stack) == 0:
                stack.append(0)
            else:
                stack.append(stack[-1])

        # Update pointer location based on direction
        pointer[0] = (pointer[0] + direction[0]) % len(code_grid)
        pointer[1] = (pointer[1] + direction[1]) % len(code_grid[pointer[0]])

    return output

class TestFunctions(unittest.TestCase):
    
    def setUp(self):
        self.str1 = ">101v>.v\nv   <  :\n>    ^ _@"
        self.str2 = ">   v>.v\nv   >   \n>      >@"
        self.str3 = ">12+.@"
        self.str4 = ">53-.@"
        self.str5 = ">62*.@"
        self.str6 = ">62/.@"
        self.str7 = ">52%.@"
        self.str8 = ">60%.@"
        self.str9 = ">0!.@"
        self.str10 = ">32`.@"
        self.str11 = ">3#2.@"
        self.str12 = ">1\\2\\...@"
        self.str13 = ">:1:...@"
        self.str14 = ">12gv\n 3v <\n a>.@"
        self.str15 = ">99*21p  v\nv        <\n>21g     .@"
        self.str16 = ">99*,@"
        self.str17 = ">9\">\",.@"
        self.str18 = "2>:3g\" \"-!v\\  g30          <\n |!`\"O\":+1_:.:03p>03g+:\"O\"`|\n @               ^  p3\\\" \":<\n2 234567890123456789012345678901234567890123456789012345678901234567890123456789"

    def tearDown(self):
        del self.str1
        del self.str2
        del self.str3
        del self.str4
        del self.str5
        del self.str6
        del self.str7
        del self.str8
        del self.str9
        del self.str10
        del self.str11
        del self.str12
        del self.str13
        del self.str14
        del self.str15
        del self.str16
        del self.str17
        del self.str18

    def test_directions(self):
        self.assertEqual(interpret(self.str1), '1', 'ERROR: Directions test #1')
        self.assertEqual(interpret(self.str2), '', 'ERROR: Directions test #2')
        pass

    def test_ops_1input(self):
        self.assertEqual(interpret(self.str9), '1', 'ERROR: Not operator incorrect')
        pass

    def test_ops_2input(self):
        self.assertEqual(interpret(self.str3), '3', 'ERROR: Addition incorrect')
        self.assertEqual(interpret(self.str4), '2', 'ERROR: Subtraction incorrect')
        self.assertEqual(interpret(self.str5), '12', 'ERROR: Multiplication incorrect')
        self.assertEqual(interpret(self.str6), '3', 'ERROR: Division incorrect')
        self.assertEqual(interpret(self.str7), '1', 'ERROR: Modulo incorrect')
        self.assertEqual(interpret(self.str8), '0', 'ERROR: Modulo 0 case incorrect')
        self.assertEqual(interpret(self.str10), '1', 'ERROR: Greater than incorrect')
        pass
        
    def test_others(self):
        self.assertEqual(interpret(self.str11), '3', 'ERROR: Trampoline incorrect')
        self.assertEqual(interpret(self.str12), '021', 'ERROR: \\ incorrect')
        self.assertEqual(interpret(self.str13), '110', 'ERROR: : incorrect')
        self.assertEqual(interpret(self.str14), '97', 'ERROR: get incorrect')
        self.assertEqual(interpret(self.str15), '81', 'ERROR: put incorrect')
        self.assertEqual(interpret(self.str16), 'Q', 'ERROR: , incorrect')
        self.assertEqual(interpret(self.str17), '>9', 'ERROR: , incorrect')
        sieve_ans = "23571113171923293137"
        self.assertEqual(interpret(self.str18), sieve_ans, 'ERROR: sieve incorrect')

######################################################################
# Run tests

if __name__ == '__main__':
    unittest.main()
