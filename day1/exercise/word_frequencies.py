f = open('/home/vattam/Desktop/circulate/word-freq/holmes.txt')

freq = {}
for line in f:
    words = line.split()
    for word in words:
        key = word.strip(',.!;?\'" ')
        if key in freq:
            freq[key] += 1
        else:
            freq[key] = 1

print freq
