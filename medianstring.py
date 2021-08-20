DNA = ['CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC','GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC','GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG']
k = 7

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

possiblekmers = Neighbors('AAAAAAA', k)

def d(pattern, DNA):
	L = len(DNA)
	k = len(pattern)
	d = float('inf')
	for i in range(L - k + 1):
		if d > hammingdistance(pattern, kmer(DNA, i, k)):
			d = hammingdistance(pattern, kmer(DNA, i, k))
	return d

def MedianString(DNA, k):
	median = str()
	L = len(DNA)
	minimumdistance = float('inf')
	for i in possiblekmers:
		matrixdistance = 0
		for j in range(L):
			matrixdistance += d(i, DNA[j])
		if minimumdistance >= matrixdistance:
			minimumdistance = matrixdistance
			median = i
	return median

print MedianString(DNA, k)