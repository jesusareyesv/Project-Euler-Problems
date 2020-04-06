def calculate_prime_numbers(n_max):
    prime_numbers = []
    end = False
    n = 2
    while not end:
        not_prime = False
        for k in prime_numbers:
            if n % k == 0:
                not_prime = True
                break

        if not not_prime:
            prime_numbers.append(n)

        n += 1
        end = len(prime_numbers) == n_max
    return prime_numbers


ps = calculate_prime_numbers(10001)
print(ps[-1])
