strand= open('rosalind_dna-2.txt').read()
adenine=0
cytosine=0
guanine=0
thymine=0
for el in strand:
    if el == 'A':
        adenine += 1
    if el == 'C':
        cytosine += 1
    if el == 'G':
        guanine += 1
    if el == 'T':
        thymine += 1
print(adenine, cytosine, guanine, thymine)