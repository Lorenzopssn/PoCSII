first_strand=open('rosalind_revc.txt').read()
first_strand=first_strand[::-1]
complementary=''
for el in first_strand:
    if el == 'A':
        complementary+='T'
    if el == 'T':
        complementary+='A'
    if el == 'C':
        complementary+='G'
    if el == 'G':
        complementary+='C'
print(complementary)

