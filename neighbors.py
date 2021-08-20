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

print len(Neighbors('TGCAT', 2))