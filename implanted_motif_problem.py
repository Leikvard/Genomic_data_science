DNA = ['CAATCGTTCTTGGGAGTGCAACGCTTACAGGCCGGCGTACAC', 'CAGACCTGGCTCACCAAAACTCTACAGATAAGCATTACCGGC', 'GCCGCAGGTGGCCAAACGGCCGGCTTTGTAACCTTCTGAGGG', 'CCGTTTATGATGGAGAGCAACGGAAACAATGCCGGCTGGGTG', 'CCGGCAACGTCCGATGCCAAATGGGGCTGTACCGGCCTGTCT', 'GAGAGCAGCACGGTGCGTTCATGGTCCGGCCTATCCAGAGCC', 'CCTAGATCATGAGCACGCTCGGTCGTTTGTGCTTCATCCGGC', 'TAATGATGACATCCGTACCTATTAGACTGTGGGATTTCCGGC', 'AGGCCGCCGATTTCCGGCGTATTCCGTCATACAATGCCAAGC', 'GAGAGCCATAAAGTAGTGTGCTCACACGTGCCCAACCCCGGC']
k = 6
d = 1

def kmer(Text, i, k):
    s = Text[i:i+k]
    return s

def hammingdistance(s1, s2):
	d = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			d = d + 1
	return d

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

def MotifEnumeration(Text, k, d):
	N = len(Text)
	patterns = []
	for i in range(N):
		DNA = Text[i]
		L = len(DNA)
		patterns.append([])
		for j in range(L - k + 1):
			pattern = kmer(DNA, j, k)
			patterns[i].extend(Neighbors(pattern, d))
	motif = set(patterns[0]) & set(patterns[1])
	for i in range(2, N):
		motif = motif & set(patterns[i])
	return motif

print MotifEnumeration(DNA, k, d)