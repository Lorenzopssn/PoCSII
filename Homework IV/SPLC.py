from Bio import SeqIO
sequences = []
f = open('rosalind_splc.txt', 'r')
for x in SeqIO.parse(f, 'fasta'):
    sequences.append(str(x.seq))
string = sequences[0]
intr = sequences[1:]
for el in intr:
    string = string.replace(el,"")
string = string.replace("T","U")
code =  {
        'UUU' : 'F', 'UUC': 'F', 
        'UUA' : 'L', 'UUG' : 'L', 
        'UCU' : 'S', 'UCA' :'S', 'UCC' : 'S', 'UCG' : 'S', 
        'UAU' : 'Y', 'UAC': 'Y', 
        'UAA': 'STOP', 'UAG': 'STOP', 
        'UGU' : 'C', 'UGC': 'C', 
        'UGA' : 'STOP', 
        'UGG': 'W', 
        'CUU' : 'L', 'CUC' : 'L', 'CUA': 'L', 'CUG': 'L', 
        'CCU': 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P', 
        'CAU' : 'H', 'CAC':'H', 
        'CAA':'Q','CAG':'Q',
        'CGU': 'R','CGC':'R','CGA':'R','CGG':'R',
        'AUU':'I','AUC':'I','AUA':'I',
        'AUG':'M',
        'ACU':'T','ACC':'T','ACA':'T','ACG':'T',
        'AAU':'N','AAC':'N',
        'AAA':'K','AAG':'K',
        'AGU':'S','AGC':'S',
        'AGA':'R','AGG':'R',
        'GUU':'V','GUC':'V','GUA':'V','GUG':'V',
        'GCU':'A','GCC':'A','GCA':'A','GCG':'A',
        'GAU':'D','GAC':'D',
        'GAA':'E','GAG':'E',
        'GGU':'G','GGC':'G','GGA':'G','GGG':'G'
}
for x in range(0, len(string) -3, 3):
    print(code[string[x: x+3]], end='')