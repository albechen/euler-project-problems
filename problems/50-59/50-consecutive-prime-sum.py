"""
Consecutive prime sum
   
Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
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


def sum_consecutive_primes(prime_range):
    max_sum = 0
    max_diff = 0
    max_range = len(prime_range)
    max_prime = max(prime_range)

    n = 0
    while n < max_range:
        run_sum = prime_range[n]
        m = n + 1
        while run_sum < max_prime:
            run_sum += prime_range[m]
            if m - n >= max_diff:
                if run_sum >= max_sum:
                    if run_sum in prime_range:
                        max_sum = run_sum
                        max_diff = m - n
            m += 1
        n += 1

    return max_sum


n_list = list_primes(1, 1000000)
sum_consecutive_primes(n_list)
# %%
