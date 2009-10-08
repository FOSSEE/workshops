def linspace(a, b, N):
    lns = []
    step = (float(b) - float(a)) / float(N - 1)
    print step
    for i in range(N):
        lns.append(a + i*step)

    return lns

print linspace(0, 5, 11)
