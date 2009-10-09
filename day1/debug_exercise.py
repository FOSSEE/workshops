import keyword
f = open('/path/to/file')

freq = {}
for line in f:
    words = line.split()
    for word in words:
        key = word.strip(',.!;?()[]: ')
        if keyword.iskeyword(key):
            value = freq[key]
            freq[key] = value + 1

print freq
