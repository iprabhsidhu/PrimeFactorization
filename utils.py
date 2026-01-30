# Utility functions

from math import sqrt, floor

def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

def primerange(lower, upper):
    prime_list = []
    for num in range(lower, upper+1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

def GIN(n) -> int:
    return floor(n)
