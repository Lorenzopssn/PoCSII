with open("rosalind_orf.txt","r") as f:
    f.readline()
    dna_string=''
    for line in f:
        dna_string+=line.strip()
def protein(smth):            
    codons = {
        "TTT":"F", "CTT":"L", "ATT":"I", "GTT":"V",
        "TTC":"F", "CTC":"L", "ATC":"I", "GTC":"V",
        "TTA":"L", "CTA":"L", "ATA":"I", "GTA":"V",
        "TTG":"L", "CTG":"L", "ATG":"M", "GTG":"V",
        "TCT":"S", "CCT":"P", "ACT":"T", "GCT":"A",
        "TCC":"S", "CCC":"P", "ACC":"T", "GCC":"A",
        "TCA":"S", "CCA":"P", "ACA":"T", "GCA":"A",
        "TCG":"S", "CCG":"P", "ACG":"T", "GCG":"A",
        "TAT":"Y", "CAT":"H", "AAT":"N", "GAT":"D",
        "TAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D",
        "TAA":"STOP", "CAA":"Q", "AAA":"K", "GAA":"E",
        "TAG":"STOP", "CAG":"Q", "AAG":"K", "GAG":"E",
        "TGT":"C", "CGT":"R", "AGT":"S", "GGT":"G",
        "TGC":"C", "CGC":"R", "AGC":"S", "GGC":"G",
        "TGA":"STOP", "CGA":"R", "AGA":"R", "GGA":"G",
        "TGG":"W", "CGG":"R", "AGG":"R", "GGG":"G"
        }
    comp = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    rRNA = ''.join(comp[el] for el in reversed(dna_string))
    rna=''.join(dna_string)
    res= []
    for x in range(len(rna)-2):
        if rna[x:x+3]=='ATG':
            temp=x
            temp2=''
            triplet='ATG'
            while codons[triplet]!="STOP":
                temp2+=codons[triplet]
                temp+=3
                if temp>len(rna)-3:
                    break
                triplet=rna[temp:temp+3]
            if codons[triplet]=="STOP" and temp2 not in res:
                res.append(temp2)
    for i in range(len(rRNA)-2):
        if rRNA[i:i+3]=='ATG':
            temp=i
            temp2=''
            triplet='ATG'
            while codons[triplet]!="STOP":
                temp2+=codons[triplet]
                temp+=3
                if temp>len(rRNA)-3:
                    break
                triplet=rRNA[temp:temp+3]
            if codons[triplet]=="STOP" and temp2 not in res:
                res.append(temp2)
    for el in res:
        print(el)
print(protein(f))