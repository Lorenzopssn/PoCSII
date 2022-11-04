from Bio import SeqIO
a = 0
b = float(0)
f = open("rosalind_tran.txt", 'r')
raw_data = list(SeqIO.parse(f, "fasta"))
f.close()
firstseq = raw_data[0].seq
secondseq = raw_data[1].seq
for el in range(len(firstseq)):
    if firstseq[el] == secondseq[el]:
        continue
    elif firstseq[el] == "A" and (secondseq[el] == "C" or secondseq[el] == "T"):
        b += 1
    elif firstseq[el] == "G" and (secondseq[el] == "C" or secondseq[el] == "T"):
        b += 1
    elif firstseq[el] == "C" and (secondseq[el] == "A" or secondseq[el] == "G"):
        b += 1
    elif firstseq[el] == "T" and (secondseq[el] == "A" or secondseq[el] == "G"):
        b += 1
    else:
        a += 1

print (a/b)