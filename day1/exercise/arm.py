cubes = []
for i in range(10):
    cubes.append(i ** 3)

for i in range(100, 1000):
    a = i % 10
    b = (i / 10) % 10
    c = (i / 100) % 10
    if i == cubes[a] + cubes[b] + cubes[c]:
        print "Armstrong Number: ", i
