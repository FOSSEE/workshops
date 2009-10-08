def gcd(a, b):
  if a % b == 0:
    return b
  return gcd(b, a%b)

print gcd(5, 40)
print gcd(11, 60)

