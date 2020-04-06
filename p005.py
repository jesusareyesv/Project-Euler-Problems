import pandas as pd


MAX_LIMIT_MULTIPLES = 20


def calculate_prime_numbers(n_max):
    prime_numbers = []
    for n in range(2, n_max + 1):
        not_prime = False
        for k in prime_numbers:
            if n % k == 0:
                not_prime = True
                break

        if not not_prime:
            prime_numbers.append(n)

    return prime_numbers


def calculate_mcd_with_primes(primes, n_max):
    result_ = []
    for i in range(2, n_max+1):
        i_dict = {}
        temp_i = i
        for p in primes:
            count_occurrences = 0
            while temp_i % p == 0:
                temp_i /= p
                count_occurrences += 1

            i_dict[str(p)] = count_occurrences

        result_.append(i_dict)
    return result_


def calculate_result(primes_, primes_occurrences_):
    result = 1
    for p in primes_:
        result *= p ** primes_occurrences_[str(p)]

    return result


primes = calculate_prime_numbers(MAX_LIMIT_MULTIPLES)
mcds = calculate_mcd_with_primes(primes, MAX_LIMIT_MULTIPLES)
df = pd.DataFrame(mcds)
primes_occurrences = df.max(axis=0)
print(calculate_result(primes,primes_occurrences))
