with open('rosalind_sseq.txt', 'r') as file:
    content = file.read()
N = content.count('>')
sequences = content.splitlines()
N_seq = 0 
my_list = []    
def motifs(data, motif):
    position = -1
    indices = ''
    for el in motif:
        position = data.find(el, position+1)
        indices += str(position+1) + ' '
    print(indices)
for el in range(N):
    DNA = ''
    N_seq += 1
    while sequences[N_seq][0] != '>':
        DNA += sequences[N_seq]
        N_seq += 1
        if N_seq+1 > len(sequences):
            break
    my_list.append(DNA)
motifs(my_list[0], my_list[1])