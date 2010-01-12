s = "1, 3-7, 12, 15, 18-21"
answer = []
single = "answer.append( %s )"
many = "answer.extend(range(%s))"
COMMA = ','
MINUS = '-'
for p in s.split(COMMA):
    if MINUS not in p:
        eval( single % (p) )
    else:
        p = p.replace( MINUS, COMMA) + '+ 1 '
        eval( many % (p) )
print answer
