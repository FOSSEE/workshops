def is_perfect_square(n):
    i = 1
    while i * i < n:
        i += 1
    return i * i == n

def all_digits_even(n):
    if n < 0: n = -n
    while n > 0:
        if n % 2 == 1:
            return False
        n /= 10
    return True

for i in range(2222, 8888):
    if all_digits_even(i) and is_perfect_square(i):
        print i
