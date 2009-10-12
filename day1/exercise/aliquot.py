def is_perfect_square(n):
    i = 1
    while i * i < n:
        i += 1
    return i * i == n, i

def aliquot(n):
    sum = 1
    i = 2

    is_ps, root = is_perfect_square(n)
    while i < root:
        if n % i == 0:
            sum += i + (n / i)
        i += 1
    return sum

n = int(raw_input('Enter a number? '))
print aliquot(n)
