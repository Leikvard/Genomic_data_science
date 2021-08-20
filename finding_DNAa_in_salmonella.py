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

L = len(seq)
candidateminskew = {0: 0}
for i in range(1, L + 1):
	candidateminskew.setdefault(i, 0)
	candidateminskew[i] = skew(seq, i)
	if candidateminskew[i] < candidateminskew[i - 1]:
		candidateminskew.pop(i - 1)

mincount = min(candidateminskew.values())
minposition = []
for i in candidateminskew:
	if count[i] == mincount:
		minposition.append(i)

print minposition

