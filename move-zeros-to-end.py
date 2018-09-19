"""
Title: Moving Zeros To The End
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
"""

def move_zeros(array):
    new_array = []
    zeros = []
    for item in array:
        if item == 0 and (type(item) == type(0) or type(item) == type(0.0)):
            zeros.append(0)
        else:
            new_array.append(item)
    return new_array + zeros

def move_zeros_refactor(array):
    non_zeros = [i for i in array if i != 0 or isinstance(i, bool)]
    return non_zeros + [0] * (len(array) - len(non_zeros))

# Tests
print(move_zeros([9,0.0,False,None,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))
print(move_zeros_refactor([9,0.0,False,None,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))
print([9,False,None,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])