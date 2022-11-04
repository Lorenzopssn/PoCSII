def mrna(string):
    codons = {'F': ['UUU', 'UUC'],
              'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
              'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
              'Y': ['UAU', 'UAC'],
              'STOP': ['UAA', 'UAG', 'UGA'],
              'C': ['UGU', 'UGC'],
              'W': ['UGG'],
              'P': ['CCU', 'CCC', 'CCA', 'CCG'],
              'H': ['CAU', 'CAC'],
              'Q': ['CAA', 'CAG'],
              'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
              'V': ['GUU', 'GUC', 'GUA', 'GUG'],
              'A': ['GCU', 'GCC', 'GCA', 'GCG'],
              'D': ['GAU', 'GAC'],
              'E': ['GAA', 'GAG'],
              'G': ['GGU', 'GGC', 'GGA', 'GGG'],
              'I': ['AUU', 'AUC', 'AUA'],
              'M': ['AUG'],
              'T': ['ACU', 'ACC', 'ACA', 'ACG'],
              'N': ['AAU', 'AAC'],
              'K': ['AAA', 'AAG']}
    RNA_num = 1
    for el in x:
        RNA_num = RNA_num * len(codons[el])
    RNA_num = RNA_num*len(codons["STOP"])
    return RNA_num % 1000000
with open("rosalind_mrna.txt", "r") as my_input:
    x= map(str, my_input.readline().strip())
RNA_num = mrna(x)
print(RNA_num)