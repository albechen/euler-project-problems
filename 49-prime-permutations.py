"""
https://projecteuler.net/problem=49
Prime permutations - Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
(i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

#%%
max_num = 10000
min_num = 1000
num_range = list(range(0, max_num))
num_range[1] = 0
n = 2
while n * n < max_num:
    x = 2
    while x < max_num / n:
        num_range[n * x] = 0
        x += 1
    n += 1

num_range = [x for x in num_range if (x >= min_num)]

#%%
sorted_split_values = []
for num in num_range:
    split_num = list([int(x) for x in str(num)])
    sorted_split_values.append(sorted(split_num))

prime_permutations = []
list_index = []

for check_1 in enumerate(sorted_split_values):
    if check_1[1] in prime_permutations:
        pass
    else:
        index_numbers = [check_1[0]]
        for check_2 in enumerate(sorted_split_values):
            if (check_1[1] == check_2[1]) & (check_1[0] != check_2[0]):
                index_numbers.append(check_2[0])
            if (len(index_numbers) >= 3) & (check_2[0] == len(sorted_split_values) - 1):
                prime_permutations.append(check_1[1])
                list_index.append(index_numbers)

#%%
primes_from_index = []
for index in list_index:
    new_list = []
    for num in index:
        new_list.append(num_range[num])
    primes_from_index.append(new_list)


for group in primes_from_index:
    test_eqi = []
    count = 1
    for x in range(0, len(group) - 1):
        y_range = range(x + 1, len(group) - 1)
        for y in y_range:
            print(x, y)
            if y != x:
                test_eqi.append(group[y] - group[x])
    for x in test_eqi:
        test_eqi_copy = test_eqi.copy()
        test_eqi_copy.remove(x)
        if x in test_eqi_copy:
            print(x, group)
