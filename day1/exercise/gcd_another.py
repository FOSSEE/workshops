def gcd(a, b):
  if a - b == 0:
    return b
  if a > b:
    return gcd(b, a-b)
  else:
    return gcd(b, b-a)

def lcm(a, b):
    return (a * b) / gcd(a, b)

print lcm(21, 14)

