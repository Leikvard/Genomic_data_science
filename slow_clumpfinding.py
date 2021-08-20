f = open('E_coli_genome.txt', 'r')
Genome = f.readline().splitlines()[0]
k = 9
L = 500
t = 3

def kmer(Text, i, k):
    s = Text[i:i+k]
    return s

def FrequentWords(Text, k, t):
    Patterns = {}   
    FrequentPatterns = list() 
    for i in range(len(Text) - k + 1):
        Patterns.setdefault(kmer(Text, i, k), 0)
        Patterns[kmer(Text, i, k)] = Patterns[kmer(Text, i, k)] + 1
    for j in Patterns:
        if Patterns[j] >= t:
            FrequentPatterns.append(j)
    return FrequentPatterns

def ClumpFinding(Text, k, L, t):
    kmers = list()
    for i in range(len(Text) - L + 1):
        window = Text[i : i + L - 1]
        kmers.extend(FrequentWords(window, k, t))
    return set(kmers)

print ClumpFinding(Genome, k, L, t)