def aliquot(n):
    """returns the aliquot of a number which
    is defined as the sum of all the proper
    divisors of a number"""
    sum = 1
    i = 2

    while i * i < n: 
        if n % i == 0:
            sum += i + (n / i)
        i += 1
    if i*i == n: sum += i
    return sum

n = int(raw_input('Enter a number? '))
print aliquot(n)
