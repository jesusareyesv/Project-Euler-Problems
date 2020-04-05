import math


# check if a number has divisors inside the primes list
def is_prime(n: int, sop: list):
    for prime in sop:
        if n % prime == 0:
            return False

    return True


N = 600851475143
upper_limit = N  # maximun range of search
test_n = 2  # I dont want to start testing primes at 1
set_of_primes = []  # It will store the found primes
prime_factors = []  # It stores the prime factors of N
while not (test_n > upper_limit):
    if is_prime(test_n, set_of_primes):
        set_of_primes.append(test_n)
        if N % test_n == 0:
            prime_factors.append(test_n)
            upper_limit = int(math.ceil(upper_limit / test_n))  # Reduces the search field knowing that you can't find
            # bigger prime factors above this limit

    test_n += 1

print(prime_factors[-1])
