"""
Prime digit replacements
   
Problem 51
By replacing the 1st digit of the 2-digit number *3, it turns out 
that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, 
this 5-digit number is the first example having seven primes among the 
ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 
56773, and 56993. Consequently 56003, being the first member of this family, 
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number 
(not necessarily adjacent digits) with the same digit, is part 
of an eight prime value family.

"""

#%%
def list_primes(min_num, max_num):
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
    return num_range

#%%
primes = list_primes(10000,99999)
n = 1
while n < 6:
    x = 0
    while x < len(primes):
        primes[x]

        x += 1


#%%
primes = list_primes(10000,99999)
primes = [x-x%1000+x%10 for x in primes]
def test_list(adj_prime_list, target_match):
    while x < target_match:
        for x in primes:

