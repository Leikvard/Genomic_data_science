import math
import random
DNA = ['AATTGGCACATCATTATCGATAACGATTCGCCGCATTGCC', 'GGTTAACATCGAATAACTGACACCTGCTCTGGCACCGCTC', 'AATTGGCGGCGGTATAGCCAGATAGTGCCAATAATTTCCT', 'GGTTAATGGTGAAGTGTGGGTTATGGGGAAAGGCAGACTG', 'AATTGGACGGCAACTACGGTTACAACGCAGCAAGAATATT', 'GGTTAACTGTTGTTGCTAACACCGTTAAGCGACGGCAACT', 'AATTGGCCAACGTAGGCGCGGCTTGGCATCTCGGTGTGTG', 'GGTTAAAAGGCGCATCTTACTCTTTTCGCTTTCAAAAAAA']
k = 6
t = 8

def kmer(text, i, k):
	s = text[i:i+k]
	return s

def Profile(matrix):
	n = len(matrix)
	k = len(matrix[0])
	a = [0.0000000000000001] * k
	c = [0.0000000000000001] * k
	g = [0.0000000000000001] * k
	t = [0.0000000000000001] * k
	for i in range(k):
		for j in range(n):
			if matrix[j][i] == 'A':
				a[i] += 1 / float(n)
			if matrix[j][i] == 'C':
				c[i] += 1 / float(n)
			if matrix[j][i] == 'G':
				g[i] += 1 / float(n)
			if matrix[j][i] == 'T':
				t[i] += 1 / float(n)
	return [a, c, g, t]

def ProfileMostProbablekmer(dna, k, m):
	L = len(dna)
	p = [1] * (L - k + 1)
	d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
	for i in range(L - k + 1):
		for j in range(k):
			p[i] *= m[d[dna[i + j]]][j]
	maxp = max(p)
	for i in range(L - k + 1):
		if p[i] == maxp:
			pattern = kmer(dna, i, k)
			break
	return pattern

def Score(matrix):
	score = 0.0
	k = len(matrix[0])
	profile = Profile(matrix)
	for i in range(k):
		for j in range(4):
			score -= profile[j][i] * math.log(profile[j][i], 2)
	return score

def RandomizedMotifSearch(dna, k, t):
	L = len(dna[0])
	bestmotifs = []
	for i in range(t):
		j = random.randint(0, L - k)
		bestmotifs.append(kmer(dna[i], j, k))
	while True:	
		profile = Profile(bestmotifs)
		motifs = []
		for j in range(t):
			motifs.append(ProfileMostProbablekmer(dna[j], k, profile))
		if Score(bestmotifs) > Score(motifs):
			bestmotifs = motifs
		else:
			return bestmotifs

bestmotifs = RandomizedMotifSearch(DNA, k, t)
i = 0
while i < 1000:
	i += 1
	motifs = RandomizedMotifSearch(DNA, k, t)
	if Score(bestmotifs) > Score(motifs):
		bestmotifs = motifs
print bestmotifs, Score(bestmotifs)