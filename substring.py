pattern = 'AA'
seq = 'TACGCATTACAAAGCACA'
d = 1

def kmer(Text, k, i):
	s = Text[i: i + k]
	return s

def hammingdistance(s1, s2):
	d = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			d = d + 1
	return d

def ApproximatePatternCount(Text, pattern, d):
	count = 0
	k = len(pattern)
	for i in range(len(Text) - k + 1):
		patternp = kmer(Text, k, i)
		if hammingdistance(patternp, pattern) <= d:
			count = count + 1
	return count

print ApproximatePatternCount(seq, pattern, d)