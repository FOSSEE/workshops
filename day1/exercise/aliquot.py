
def aliquot(n):
    sum = 1
    i = 2

    while i * i < n: 
        if n % i == 0:
            sum += i + (n / i)
        i += 1
    if n % i == 0: sum += i
    return sum

n = int(raw_input('Enter a number? '))
print aliquot(n)
