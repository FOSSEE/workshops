from pylab import *
from scipy import *
from scipy import stats

scores = [[], [], [], [], []]
ninety_percents = [{}, {}, {}, {}, {}]

for record in open('sslc1.txt'):
    record = record.strip()
    fields = record.split(';')

    region_code = fields[0].strip()
   
    for i, field in enumerate(fields[3:8]):
        if region_code not in ninety_percents[i]:
            ninety_percents[i][region_code] = 0
        score_str = field.strip()
        score = 0 if score_str == 'AA' else int(score_str)
        scores[i].append(score)
        if score > 90:
            ninety_percents[i][region_code] += 1

subj_total = []
for subject in ninety_percents:
    subj_total.append(sum(subject.values()))


figure(1)
pie(ninety_percents[3].values(), labels=ninety_percents[3].keys())
title('Students scoring 90% and above in science by region')
savefig('/tmp/science.png')

figure(2)
pie(subj_total, labels=['English', 'Hindi', 'Maths', 'Science', 'Social'])
title('Students scoring more than 90% by subject(All regions combined).')
savefig('/tmp/all_regions.png')

math_scores = array(scores[2])
# Mean score in Maths(All regions combined)
print "Mean: ", mean(math_scores)

# Median score in Maths(All regions combined)
print "Median: ", median(math_scores)

# Mode score in Maths(All regions combined)
print "Mode: ", stats.mode(math_scores)

# Standard deviation of scores in Maths(All regions combined)
print "Standard Deviation: ", std(math_scores)

