import math
f = open('E_coli_genome.txt', 'r')
seq = f.readline().splitlines()[0]
k = 9
L = 500
t = 3


def kmer(Text, i, k):
    s = Text[i:i+k]
    return s

def PatternToNumber(text):
	l = len(text)
	d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
	number = 0
	for i in range(l):
		base = text[i]
		number = number + d[base] * int(math.pow(4, l - i - 1))
	return number

def NumberToPattern(number, k):
	d = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
	pattern = ''
	for i in range(k):
		remain = number % 4
		pattern = d[remain] + pattern
		number = number // 4
	return pattern

def ComputingFrequencies(Text, k):
	FrequencyArray = {}
	for i in range(len(Text) - k + 1):
		pattern = kmer(Text, i, k)
		FrequencyArray.setdefault(pattern, 0)
		FrequencyArray[pattern] = FrequencyArray[pattern] + 1
	return FrequencyArray

def ClumpFinding(Text, k, L, t):
	frequentpatterns = {}
	firstwindow = Text[0: L]
	frequencyarray = ComputingFrequencies(firstwindow, k)
	for i in frequencyarray:
		if frequencyarray[i] >= t:
			frequentpatterns[i] = 1
	for i in range(L, len(Text) - k - L + 1):
		firstkmer = kmer(Text, i - L, k)
		lastkmer = kmer(Text, i - k + 1, k)
		frequencyarray[firstkmer] = frequencyarray[firstkmer] - 1
		frequencyarray.setdefault(lastkmer, 0)
		frequencyarray[lastkmer] = frequencyarray[lastkmer] + 1
		if frequencyarray[lastkmer] >= t:
			frequentpatterns[lastkmer] = 1
	return frequentpatterns.keys(), len(frequentpatterns.keys())

print ClumpFinding(seq, k, L, t)
