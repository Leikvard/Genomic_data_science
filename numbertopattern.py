def NumberToPattern(number, k):
	d = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
	pattern = ''
	for i in range(k):
		remain = number % 4
		pattern = d[remain] + pattern
		number = number // 4
	return pattern

print NumberToPattern(6801, 11)