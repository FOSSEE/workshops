# Armstrong Numbers

for n in range(100, 1000):
#    s = str(n)
#    a, b, c = int(s[0]), int(s[1]), int(s[2])
#    if a * a * a + b * b * b + c * c * c == n:
#       print n
#   sum, copy = 0, n    
#   while copy > 0:
#       sum += (copy % 10) ** 3
#       copy /= 10
#   if sum == n:
#      print n
    u = n % 10
    h = n / 100
    t = (n/10) % 10
    if h ** 3 + t ** 3 + u ** 3 == N:
        print n 
