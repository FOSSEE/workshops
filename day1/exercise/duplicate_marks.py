students = {
    'Madhu': 45,
    'Shantanu':45,
    'Puneeth': 54,
    'Vattam': 35,
    'KD': 54,
    'Asokan': 45
    }

all_marks = students.values()
unique_marks = set(all_marks)

print "Number of Duplicate marks: ", len(all_marks) - len(unique_marks)

for i in unique_marks:
    all_marks.remove(i)

print "Duplicate marks:", set(all_marks)
