def generate_fib(limit=4000000):
    succ = []
    a, b = 1, 1
    while a < limit:
        succ.append(a)
        a, b = b, a + b
    return succ

print(generate_fib())
print(sum(filter(lambda x: x % 2 == 0, generate_fib())))
