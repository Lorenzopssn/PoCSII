from Bio import SeqIO
from math import factorial 
f = open('rosalind_pmch.txt', 'r')
inp = ''
AU_content = 0
GC_content = 0
for i in SeqIO.parse(f, 'fasta'):
    inp = str(i.seq)
for el in inp:
    if el == 'A':
        AU_content += 1
    elif el == 'G':
        GC_content += 1
print((factorial(AU_content) * factorial(GC_content)))