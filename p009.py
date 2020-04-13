import math


def is_triangular(a, b, c):
    return (a**2 + b**2) == c**2


def ismile(a, b, c):
    return (a + b + c) == 1000


count = 0
for a in range(1, 1001):
    for b in range(a+1, 1001):
        for c in range(b+1, 1001):
            if ismile(a, b, c):
                if is_triangular(a, b, c):
                    print(a, b, c)

print(count)
# 200 375 425
