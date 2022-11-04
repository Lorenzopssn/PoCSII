from Bio import SeqIO
a = []  
b = []
f = open('rosalind_grph.txt', 'r')  #I open my file
for el in SeqIO.parse(f, 'fasta'):
    count1 = 0
    count2 = 0
    my_prefiix = [el.id]
    my_suffix = [el.id]
    pre = ''
    suf = ''
    for x in el.seq:
        if count1 < 3:
            pre += x
            count1 += 1
    my_prefiix.append(pre)
    for y in reversed(el.seq):
        if count2 < 3:
            suf += y
            count2 += 1                                                
    my_suffix.append(''.join(reversed(suf)))
    b.append(my_prefiix)
    a.append(my_suffix)
f.close()                                                                      
for x, y in enumerate(a):
    suff = a[x][1]
    id = a[x][0]
    for c, d in enumerate(b):
        if suff == b[c][1] and id != b[c][0]:
            print(id, b[c][0])