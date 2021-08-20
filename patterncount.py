def kmer(Text, i, k):
    s = Text[i:i+k]
    return s

def PatternCount(Text, pattern):
    count = 0
    for i in range(len(Text) - len(pattern) + 1):
        if kmer(Text, i, len(pattern)) == pattern:
            count = count + 1
    return count