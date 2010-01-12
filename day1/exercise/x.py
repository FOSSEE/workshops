d1 = [2,4,6,8]
d0 = [0,2,4,6,8]
dq = [0, 4, 6]

for a in d1:
    th = a * 1000
    for b in d0:
        hu = b * 100
        for c in d0:
            te = c * 10
            for u in dq:
                n = th + hu + te + u
                if is_square(n): print n


for i in range(46, 94, 2):
    n = i * i
    if all_even( n ): print n

