f = open('Salmonella_enterica_genome.txt', 'r')
seq = ''.join(line.rstrip() for line in f)

def skew(Text, i):
	d = {'A': 0, 'C': -1, 'G': 1, 'T': 0}
	L = len(Text)
	count = 0
	if i == 0:
		return count
	for j in range(0, i):
		count += d[Text[j]]
	return count

count = []
for i in range(len(seq) + 1):
	count.append(skew(seq,i))

mincount = min(count)
for i in range(len(count)):
	if count[i] == mincount:
		print i
