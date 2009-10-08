r, c = 5, 4
for i in range(1, 9):
    for j in range(1, 9):
        a = r - i
        b = c - j
        if a and b and a == b or a == -b:
            print i, j
