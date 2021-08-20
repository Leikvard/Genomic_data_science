def kmer(Text, i, k):
    s = Text[i:i+k]
    return s

def FrequentWords(Text, k):
    Patterns = {}   
    FrequentPatterns = list() 
    for i in range(len(Text) - k + 1):
        Patterns.setdefault(kmer(Text, i, k), 0)
        Patterns[kmer(Text, i, k)] = Patterns[kmer(Text, i, k)] + 1
    Counts = Patterns.values()
    MaxCount = max(Counts)
    for j in Patterns:
        if Patterns[j] == MaxCount:
            FrequentPatterns.append(j)
    return FrequentPatterns, MaxCount
