import math

def linspace(a, b, N):
    lns = []
    step = (float(b) - float(a)) / float(N - 1)
    print step
    for i in range(N):
        lns.append(a + i*step)

    return lns

def sinsin_func():
    x = linspace(0, 5, 11)
    sin_list = []
    for i in x:
        sin_list.append(math.sin(i) + math.sin(10*i))

    return sin_list

def find_root_range():
    sin_list = sinsin_func()
    for i, sins in enumerate(sin_list):
        if (sin_list[i] > 0 and sin_list[i+1] < 0) or (sin_list[i] > 0 and sin_list[i+1] < 0):
            print "Roots lie between: %f and %f" % (sin_list[i], sin_list[i+1])
        if sin_list[i] == 0:
            print "%f is the root" % sin_list[i]

find_root_range()
