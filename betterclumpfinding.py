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

def ComputingFrequencies(Text, k):
	FrequencyArray = [0] * int(math.pow(4, k))
	for i in range(len(Text) - k + 1):
		pattern = kmer(Text, i, k)
		j = PatternToNumber(pattern)
		FrequencyArray[j] = FrequencyArray[j] + 1
	return FrequencyArray

def ClumpFinding(Text, k, L, t):
	Count = [0] * int(math.pow(4, k))
	frequentpatterns = list()
	firstwindow = Text[0: L - 1]
	frequencyarray = ComputingFrequencies(firstwindow, k)
	for i in range(L):
		if frequencyarray[i] >= t:
			Count[i] = 1
	for i in range(L, len(Text) - k - L + 1):
		firstkmer = kmer(Text, i - L, k)
		firstindex = PatternToNumber(firstkmer)
		lastkmer = kmer(Text, i - k + 1, k)
		lastindex = PatternToNumber(lastkmer)
		frequencyarray[firstindex] = frequencyarray[firstindex] - 1
		frequencyarray[lastindex] = frequencyarray[lastindex] + 1
		if frequencyarray[lastindex] >= t:
			Count[lastindex] = 1
	for i in range(int(math.pow(4, k))):
		if Count[i] == 1:
			pattern = NumberToPattern(i, k)
			frequentpatterns.append(pattern)
	return frequentpatterns, len(frequentpatterns)

print ClumpFinding(seq, k, L, t)
