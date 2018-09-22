"""
Title: Primes in numbers
Given a positive number n > 1 find the prime factor decomposition of n.
The result will be a string with the following form : "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.
"""

import math

def stringFactors(list_factors):
    """
    Takes ordered list, groups into distinct factors, and returns string
    """
    output_string = ""
    distinct_factors = set(list_factors)
    for factor in sorted(distinct_factors):
        if list_factors.count(factor) == 1:
            output_string = output_string + "(" + str(factor) + ")"
        else:
            output_string = output_string + "(" + str(factor) + "**" + str(list_factors.count(factor)) + ")"
    return output_string

def primeFactors(num):
    """
    Takes number and returns prime factor decomposition as string
    """
    working_num = num
    factors = []
    for i in range(2, working_num + 1):
        while working_num % i == 0:
            factors.append(i)
            working_num /= i
        if working_num == 1:
            return stringFactors(factors)
    return stringFactors(factors)

# Tests
print(primeFactors(7775460) == "(2**2)(3**3)(5)(7)(11**2)(17)")