def aliquot(n):
    sum = 1
    i = 2

    while i * i  < n:
        if n % i == 0:
            sum += i + (n / i)
        i += 1
    return sum

amicable = []

n = 1000
while n < 10000:
    m = aliquot(n)
    if m > n and aliquot(m) == n:
        print m, n
    n += 1
