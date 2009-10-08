import math

def aliquot(n):
    sum = 0
    for i in range(1, math.sqrt(n)+1):
        if n % i == 0:
            sum += i + n/i
    return sum

amicable = []
for n in range(10000, 100000):
    m = aliquot(n)
    if aliquot(m) == n:
        amicable.append((m, n))

print amicable

# please please please profile this.
