"""
https://projecteuler.net/problem=3
Problem 3 - Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
#%%
import numpy as np


def multiply_list(list):
    product = 1
    for x in list:
        product = product * x
    return product


def return_prime_factors(number):
    currentNumber = number
    fullPrimeFactors = False
    primeFactorList = []
    n = 2

    while fullPrimeFactors == False:
        if currentNumber % n == 0:
            currentNumber = currentNumber / n
            primeFactorList.append(n)
            if int(multiply_list(primeFactorList)) == number:
                fullPrimeFactors = True
        if n == 2:
            n = n + 1
        else:
            n = n + 2

    return primeFactorList


return_prime_factors(600851475143)

# %%
