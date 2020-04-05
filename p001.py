import math
sum_ = 0
for n in range(1000):
    sum_ += (n % 3 == 0 or n % 5 == 0) and n or 0

print(sum_)
