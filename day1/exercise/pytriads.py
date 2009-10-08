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

for a in range(3, 100):
    for b in range(a+1, 100):
        ips, c = is_perfect_square((a * a) + (b * b))
        if ips and gcd(a, b) == 1:
            print a, b, c

