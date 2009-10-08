students = {
    'Madhu': 12,
    'Shantanu':45,
    'Puneeth': 54,
    'Vattam': 35,
    'KD': 50,
    }

all_marks = students.values()
unique_marks = set(all_marks)

print "Number of Duplicate marks: ", len(all_marks) - len(unique_marks)
print "Duplicate marks: ", set(all_marks - list(unique_marks))
