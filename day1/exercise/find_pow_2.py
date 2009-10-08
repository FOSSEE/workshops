def is_pow_2(n):
    bin_count = 0
    while n > 0:
        if n % 2 == 1:
            bin_count += 1
        if bin_count > 1:
            return False
        n /= 2

    return bin_count == 1

def collatz_pow_2(n):
    if n == 1: return 4
    if n == 2: return 4
    collatz_pow_2 = []
    while n > 2:
        print n, 
        if is_pow_2(n):
            collatz_pow_2.append(n)

        if n % 2:
            n = n * 3 - 1
        else:
            n /= 2 

    return max(collatz_pow_2)

import sys
collatz_pow_2(int(sys.argv[1]))
