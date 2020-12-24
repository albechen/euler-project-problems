"""
https://projecteuler.net/problem=48
Self powers - Problem 48

The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""

#%%
def sum_self_power_last_10_digits(max_num):
    current_sum = 0
    num = 1
    while num <= max_num:
        current_product = num
        count = 1
        while count < num:
            current_product = (current_product * num) % 10000000000
            count += 1
        current_sum = (current_product + current_sum) % 10000000000
        num += 1
    print(current_sum)
    return current_sum


# %%
sum_self_power_last_10_digits(10001000)
# %%
