"""
Problem 5 - Smallest multiple

2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by
all of the numbers from 1 to 20?
"""

#%%
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


def multiply_list(list):
    product = 1
    for x in list:
        product = product * x
    return product


def smallest_divisable_num(highestNumber):
    primeFactorList = []
    for n in range(2, highestNumber + 1):
        print(n)
        nPrimeFactors = return_prime_factors(n)
        print(nPrimeFactors)
        primeFactorList = primeFactorList + list(
            set(nPrimeFactors) - set(primeFactorList)
        )
    smallestDivisable = multiply_list(primeFactorList)
    return smallestDivisable


smallest_divisable_num(20)

# %%
return_prime_factors(50)

# %%
