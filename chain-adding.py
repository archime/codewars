"""
Title: A chain adding function
We want to create a function that will add numbers together when called in succession.
add(1)(2);
// returns 3

We also want to be able to continue to add numbers to our chain.
add(1)(2)(3); // 6
add(1)(2)(3)(4); // 10
add(1)(2)(3)(4)(5); // 15
and so on.
"""

class add:
    
    def __init__(self, value = 0):
        self.value = value
    
    def __str__(self):
        return str(self.value)
    
    def __call__(self, value):
        new_value = self.value + value
        return add(new_value)
    
    def __eq__(self, other):
        if self.value == other:
            return True
        return False
    
    def __add__(self, other):
        return self.value + other
    
    def __sub__(self, other):
        return self.value - other

# Tests
print(add(1) == 1)
print(add(1)(2) == 3)
print(add(1)(1) + 1 == 3)
print(add(1)(1) - 1 == 1)
addTwo = add(2)
print(addTwo + 5 == 7)
print(addTwo(3) == 5)
print(addTwo(3)(5) == 10)