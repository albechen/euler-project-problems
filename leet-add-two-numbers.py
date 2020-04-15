"""
You are given two non-empty linked lists representing two 
non-negative integers. The digits are stored in reverse order 
and each of their nodes contain a single digit. Add the two 
numbers and return it as a linked list.

You may assume the two numbers do not contain any leading 
zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""
#%%
def addTwoNumbers(l1, l2):
    len_diff = len(l2) - len(l1)
    if len_diff > 0:
        for l in range(len_diff):
            l1.append(0)
    elif len_diff < 0:
        len_diff *= -1
        for l in range(len_diff):
            l2.append(0)

    print(l1, l2)

    sum_list = []
    z_big = 0
    for x, y in zip(l1, l2):
        z = x + y + z_big
        if z >= 10:
            z_small = z % 10
            z_big = (z - z_small) / 10
            z = z_small
        else:
            z_big = 0
        z = int(z)
        sum_list.append(z)

    return sum_list


l1 = [2, 4, 3, 6]
l2 = [5, 6, 4]

addTwoNumbers(l1, l2)


# %%
