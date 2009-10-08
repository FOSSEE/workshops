import math

def linspace(a, b, N):
    lns = []
    step = (float(b) - float(a)) / float(N - 1)
    print step
    for i in range(N):
        lns.append(a + i*step)

    return lns

def sin_func():
    x = linspace(0, 5, 11)
    sin_list = []
    for i in x:
        sin_list.append(math.sin(i))

    print sin_list

def sinsin_func():
    x = linspace(0, 5, 11)
    sin_list = []
    for i in x:
        sin_list.append(math.sin(i) + math.sin(10*i))

    print sin_list

sinsin_func()
