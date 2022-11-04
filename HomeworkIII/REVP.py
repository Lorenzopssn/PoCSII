from Bio import SeqIO

def reverse(inp):
    inp = inp[::-1]
    final = ''
    for a in range(len(x)):
        if x[a] == 'A':
            final += 'T'
        elif x[a] == 'T':
            final += 'A'
        elif x[a] == 'G':
            final += 'C'
        elif x[a] == 'C':
            final += 'G'
    return final

def palindrome(x):
    for a in range(len(x)):
        for b in range(4,13,1):
            if x[a:a+b] == reverse(x[a:a+b]) and (a+b <= len(x)):
                print(a+1, b)

if __name__ == "__main__":
    seq_name, seq_string = [], []
    with open ("rosalind_revp.txt",'r') as my_sample:
        for seq_record  in SeqIO.parse(my_sample,'fasta'):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq))
    x = seq_string[0]
    palindrome(x)
