"""
Permuted multiples
   
Problem 52
It can be seen that the number, 125874, and its
double, 251748, contain exactly the same digits,
but in a different order.

Find the smallest positive integer, x, such that
2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

#%%
def match_num_pair(num1, num2):
    list1 = list(str(num1))
    list1.sort()
    list2 = list(str(num2))
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False


def check_num_mulp(num1, target_mulp):
    equal = True
    n = 1
    while equal == True:
        for x in range(target_mulp + 1)[:1:-1]:
            num2 = x * num1
            if match_num_pair(num1, num2) == False:
                return False
            else:
                n += 1
            if n > target_mulp:
                return True


def smallest_integer_permutated_multiples(target_mulp):
    equal = True
    n = 1
    while equal == True:
        if check_num_mulp(n, target_mulp) == True:
            return n
        n += 1


smallest_integer_permutated_multiples(6)
