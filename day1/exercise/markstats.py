import math

f = open('/home/madhu/Desktop/marks.dat')
    
subj_marks = [[]] * 5
names = []
for line in f:
    fields = line.split(';')
    names.append(fields[2])
    for i in range(5):
        subj_marks[i].append(int(fields[i+3]))

for i in range(5):
    avg_marks = float(sum(subj_marks[i])) / len(subj_marks[i])
    student = names[subj_marks[i].index(max(subj_marks[i]))]
    sigma = 0
    for j in subj_marks[i]:
        sigma += (j - avg_marks) ** 2

    std_dev = math.sqrt(sigma)
    print "Average marks for subject: %f is Standard Deviation is %f, Student with Highest Marks is %s" % (avg_marks, std_dev, student)

