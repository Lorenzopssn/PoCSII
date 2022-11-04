RNA=open('rosalind_prot.txt').read()
n=3
protein_string=''
codon_seq=[RNA[i:i+n]for i in range (0,len(RNA)-2,n)]
codon_map=open('PROT.txt').readlines()
dictionary={}
for el in codon_map:
    el=el.strip().split()
    dictionary[el[0]]=el[1]
for el in codon_seq:
    if el in dictionary:
        protein_string=protein_string+dictionary.get(el)
print(protein_string)

    

