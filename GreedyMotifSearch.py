import math
DNA = ["ATGACCGGGATACTGATAGAAGAAAGGTTGGGGGCGTACACATTAGATAAACGTATGAAGTACGTTAGACTCGGCGCCGCCG", "ACCCCTATTTTTTGAGCAGATTTAGTGACCTGGAAAAAAAATTTGAGTACAAAACTTTTCCGAATACAATAAAACGGCGGGA", "TGAGTATCCCTGGGATGACTTAAAATAATGGAGTGGTGCTCTCCCGATTTTTGAATATGTAGGATCATTCGCCAGGGTCCGA", "GCTGAGAATTGGATGCAAAAAAAGGGATTGTCCACGCAATCGCGAACCAACGCGGACCCAAAGGCAAGACCGATAAAGGAGA", "TCCCTTTTGCGGTAATGTGCCGGGAGGCTGGTTACGTAGGGAAGCCCTAACGGACTTAATATAATAAAGGAAGGGCTTATAG", "GTCAATCATGTTCTTGTGAATGGATTTAACAATAAGGGCTGGGACCGCTTGGCGCACCCAAATTCAGTGTGGGCGAGCGCAA", "CGGTTTTGGCCCTTGTTAGAGGCCCCCGTATAAACAAGGAGGGCCAATTATGAGAGAGCTAATCTATCGCGTGCGTGTTCAT", "AACTTGAGTTAAAAAATAGGGAGCCCTGGGGCACATACAAGAGGAGTCTTCCTTATCAGTTAATGCTGTATGACACTATGTA", "TTGGCCCATTGGCTAAAAGCCCAACTTGACAAATGGAAGATAGAATCCTTGCATACTAAAAAGGAGCGGACCGAAAGGGAAG" , "CTGGTGAGCAACGACAGATTCTTACGTGCATTAGCTCGCTTCCGGGGATCTAATAGCACGAAGCTTACTAAAAAGGAGCGGA"]
k = 15
t = 10

def kmer(text, i, k):
	s = text[i:i+k]
	return s

def Profile(matrix):
	n = len(matrix)
	k = len(matrix[0])
	a = [0.00000000000000000001] * k
	c = [0.00000000000000000001] * k
	g = [0.00000000000000000001] * k
	t = [0.00000000000000000001] * k
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

def GreedyMotifSearch(dna, k, t):
	bestmotifs = []
	L = len(dna[0])
	for i in range(t):
		bestmotifs.append(kmer(dna[i], 0, k))
	for i in range(L - k + 1):
		motifs = []
		motifs.append(kmer(dna[0], i, k))
		profile = Profile(motifs)
		for j in range(1, t):
			motifs.append(ProfileMostProbablekmer(dna[j], k, profile))
			profile = Profile(motifs)
		if Score(bestmotifs) > Score(motifs):
			bestmotifs = motifs
	return bestmotifs, Score(bestmotifs)


print GreedyMotifSearch(DNA, k, t)