def all_digits_even(n):
    if n < 0: n = -n
    while n > 0:
        if n % 2 == 1:
            return False
        n /= 10
    return True

i = 46
while i <= 94:
    square = i * i
    if all_digits_even(square):
        print square
    i += 1
