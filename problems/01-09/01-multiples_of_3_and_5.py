"""
https://projecteuler.net/problem=1
Problem 1 - Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
#%%
def get_multiples(num, maxNumber):
    maxNumber = maxNumber - 1
    maxMultiple = int(maxNumber / num - (maxNumber / num) % 1)
    rangeMultiple = list(range(1, maxMultiple + 1))
    finalMultiple = [x * num for x in rangeMultiple]
    return finalMultiple


def combine_lists_remove_duplicates(list1, list2):
    fullList = list(set(list1 + list2))
    sumList = sum(fullList)
    return sumList


multiples_3 = get_multiples(3, 1000)
multiples_5 = get_multiples(5, 1000)
combine_lists_remove_duplicates(multiples_3, multiples_5)
# %%