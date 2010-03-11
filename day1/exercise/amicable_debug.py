import math

def aliquot(n):
    sum = 1
    i = 2

    while i * i < n: 
        if n % i == 0:
            sum += i + (n / i)
        i += 1
    if i*i == n: sum += i
    return sum

amicable = []
for n in range(1000, 10000):
    m = aliquot(n)
    if m > n and aliquot(m) == n:
        amicable.append((m, n))

print amicable

# please please please profile this.
