cubes = []
for i in range(10):
    cubes.append(i ** 3)

for i in range(100, 1000):
    ones = i % 10
    tens = (i / 10) % 10
    hundreds = (i / 100) % 10
    if i == cubes[ones] + cubes[tens] + cubes[hundreds]:
        print "Armstrong Number: ", i
