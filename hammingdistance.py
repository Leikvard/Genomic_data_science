seq1 = 'CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT'
seq2 = 'CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG'

def hammingdistance(s1, s2):
	d = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			d = d + 1
	return d

print hammingdistance(seq1, seq2)
