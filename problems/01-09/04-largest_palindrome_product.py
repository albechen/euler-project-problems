"""
https://projecteuler.net/problem=4
Problem 4 - Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
#%%
import numpy as np


def check_palindrome(number):
    stringNumber = str(number)
    return stringNumber == stringNumber[::-1]


listDigits = list(range(100, 1000))
palList = []
xyList = []
for x in listDigits:
    for y in listDigits:
        if check_palindrome(x * y) == True:
            palList.append(x * y)
            xyList.append([x, y])

print(max(palList))
xyList[palList.index(max(palList))]
# %%
