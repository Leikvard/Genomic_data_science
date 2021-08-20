# f = open('dataset_9_4.txt', 'r')
seq = 'TCCGTAGGTAGGTAGGTCCGTAGGACACACACTCCGGTCTAGGGTCTAGGTAGGTAGGTCCGTAGGTAGGTCCGACACACACTCCGTAGGTAGGTAGGACACTCCGACACGTCTCCGTAGGTCCGTCCGACACTAGGTAGGTCCGTAGGTAGGGTCTCCGGTCTCCGTAGGGTCTAGGTCCGTCCGTAGGGTCGTCACACTCCGTAGGACACTAGGTCCGACACTAGGTCCGTCCGTAGGGTCTCCGTAGGTAGGGTCGTCTAGGTAGGTCCGACACTAGGTAGGTCCGGTCTAGGTAGGTAGGACACTAGGACACTCCGGTCTAGGTCCGTCCGTAGGACACACACTAGGTCCGTCCGTAGGGTCTAGGTAGGTAGG'
k = 5
d = 3
# f.close

def kmer(Text, k, i):
	s = Text[i: i + k]
	return s

def hammingdistance(s1, s2):
	d = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			d = d + 1
	return d

def PatternToNumber(text):
	l = len(text)
	d = {'A': 0, 'a': 0, 'C': 1, 'c': 1, 'G': 2, 'g': 2, 'T': 3, 't': 3}
	number = 0
	for i in range(l):
		base = text[i]
		number = number + d[base] * math.pow(4, l - i - 1)
	return int(number)

def NumberToPattern(number, k):
	d = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
	pattern = ''
	for i in range(k):
		remain = number % 4
		pattern = d[remain] + pattern
		number = number // 4
	return pattern

def Neighbors(pattern, d):
	if d == 0:
		return [pattern]
	if len(pattern) == 1:
		return ['A', 'T', 'C', 'G']
	neighborhood = []
	L = len(pattern)
	sufpattern = pattern[1:]
	sufneighbor = Neighbors(sufpattern, d)
	for i in sufneighbor:
		if hammingdistance(i, sufpattern) == d:
			neighborhood.append(pattern[0] + i)
		if hammingdistance(i, sufpattern) < d:
			for j in ['A', 'C', 'G', 'T']:
				neighborhood.append(j + i)
	return set(neighborhood)

def ApproFreqPatternCount(Text, k, d):
	count = {}
	L = len(Text)
	frequentpatterns = []
	for i in range(L - k + 1):
		pattern = kmer(Text, k, i)
		count.setdefault(pattern, 0)
		for j in Neighbors(pattern, d):
			count.setdefault(j, 0)
			count[j] += 1
	maxcount = max(count.values())
	for i in count:
		if count[i] == maxcount:
			frequentpatterns.append(i)
	return frequentpatterns
	
print hammingdistance('CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT', 'CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG')
