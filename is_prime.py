"""
Define a function isPrime/is_prime() that takes one integer argument and returns 
True or False depending on if the integer is a prime.
"""

def is_prime(num):
  if num <= 1:
  	return False
  else:
  	for div in range(2, num):
  		if num % div == 0:
  			return False
  return True