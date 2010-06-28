num = int( raw_input( 'Enter number: ') )
while num != 4:
    print num,
    if num % 2 == 1:
        num = num * 3 + 1
    else:
        num /= 2
print 4, 2, 1
