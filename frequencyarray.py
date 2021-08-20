import math
f = open('dataset_2994_5.txt', 'r')
seq = f.readline().splitlines()[0]
k = 6

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

def ComputingFrequencies(Text, k):
	FrequencyArray = [0] * int(math.pow(4, k))
	for i in range(len(Text) - k + 1):
		pattern = kmer(Text, i, k)
		j = PatternToNumber(pattern)
		FrequencyArray[j] = FrequencyArray[j] + 1
	return FrequencyArray

print " ".join(map(str, ComputingFrequencies(seq, k)))