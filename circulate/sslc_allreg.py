
math_scores = []
for record in open('sslc1.txt'):
    fields = record.split(';')

    math_score = fields[5].strip()
    if math_score != 'AA':
        math_scores.append(int(math_score))
    else:
        math_scores.append(0)


# List method
print "Mean: ", mean(math_scores)

print "Median: ", median(math_scores)

print "Standard Deviation: ", std(math_scores)

# Array method

math_scores = array(math_scores)

print "Mean: ", mean(math_scores)

print "Median: ", median(math_scores)

print "Standard Deviation: ", std(math_scores)

