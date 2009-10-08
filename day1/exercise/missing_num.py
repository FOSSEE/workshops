str_range = '4-7, 9, 12, 15'

ranges = str_range.split(',')

lst = []
for r in ranges:
    vals = r.split('-')
    if len(vals) == 2:
       lst.extend(range(int(vals[0]), int(vals[1]) + 1))
    else:
       lst.append(int(vals[0]))

set_range = set(lst)
all_elems = set(range(min(lst), max(lst)))

print all_elems - set_range
