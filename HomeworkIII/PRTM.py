protein_seq=open('rosalind_prtm.txt').read()
weight_table=open('weighted_amino_acids.txt').readlines()
total_weight=0
dictionary={}
for el in weight_table:
    el=el.strip().split()
    dictionary[el[0]]=float(el[1])
for x in protein_seq[:-1]:
    total_weight += dictionary.get(x)
print('{0:.4f}'.format(total_weight))