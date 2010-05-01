anag = {}
for line in open( 'anag.txt'):
	word = line.strip()
	key = ''.join(sorted(list(word)))
	if key not in anag:
		anag[ key ] = [ word ]
	else:
		anag[key].append(word)
for key in anag:
	if len(anag[key]) > 1:
		print anag[key]
         