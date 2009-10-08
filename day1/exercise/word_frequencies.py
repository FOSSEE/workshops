f = open('/home/madhu/pyprogs/pytriads.py')

freq = {}
for line in f:
    words = line.split()
    for word in words:
        key = word.strip(',.!;?\'" ')
        value = freq.get(key, 1)
        freq[key] = value + 1

print freq
