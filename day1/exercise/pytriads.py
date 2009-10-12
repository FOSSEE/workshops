def is_perfect_square(n):
    i = 1
    while i * i < n:
        i += 1
    return i * i == n, i

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

a = 3
while a < 100:
    b = a + 1
    while b < 100:
        is_ps, c = is_perfect_square((a * a) + (b * b))
        if is_ps and gcd(a, b) == 1:
            print a, b, c
        b += 1
    a += 1
