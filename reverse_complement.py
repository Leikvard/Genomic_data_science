f = open("dataset_3_2.txt", 'r')

Seq = f.readline().splitlines()[0]

def ReverseComplement(Text):
    PatternRC = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    RC = ''
    for i in range(len(Text)):
        RC = RC + PatternRC[Text[len(Text) - i - 1]]
    return RC

print ReverseComplement(Seq)
