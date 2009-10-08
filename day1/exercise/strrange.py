str_ranges = "1, 3-7, 12, 15, 18-21"

ranges = str_ranges.split(',')

lst = []
for r in ranges:
    vals = r.split('-')
    if len(vals) == 2:
       lst.extend(range(int(vals[0]), int(vals[1]) + 1))
    else:
       lst.append(int(vals[0]))

print lst
