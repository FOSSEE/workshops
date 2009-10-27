import keyword
f = open('amicable.py')

freq = {}
for line in f:
    words = line.split()
    for word in words:
        key = word.strip(',.!;?()[]: ')
        if keyword.iskeyword(key):
            if key in freq:
                freq[key] += 1
            else:
                freq[key] = 1

print freq

