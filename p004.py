def is_palindrome(n: int):
    n_ = str(n)
    reversed_ = ''.join(list(reversed(n_)))
    return n_ == reversed_


largest_palindrome = None
b_limit = 0
for i in range(999):
    largest_palindrome_i = None
    a, b = 0, 0
    for k in range(999):
        a, b = 999 - i, 999 - k
        if b < b_limit:
            break
        prod = a * b
        if is_palindrome(prod):
            largest_palindrome_i = prod
            break

    if largest_palindrome_i:
        if (not largest_palindrome) or largest_palindrome_i >= largest_palindrome:
            largest_palindrome = largest_palindrome_i
            b_limit = b
        else:
            break

print(largest_palindrome)

