f = open('/home/madhu/Desktop/marks.dat')

for line in f:
    fields = line.split(';')
    print "Name: %s, Total Marks: %s" % (fields[2].strip(), fields[8].strip())
