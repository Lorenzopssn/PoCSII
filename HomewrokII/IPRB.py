inp=open('rosalind_iprb.txt').read().split()
k,m,n=int(inp[0]),int(inp[1]),int(inp[2])
tot=k+m+n
rec_homo=(n/tot)*((n-1)/(tot-1))
heterozygous=(m/tot)*((m-1)/(tot-1))
recessive=(n/tot)*(m/(tot-1))+(m/tot)*(n/(tot-1))
my_prob=rec_homo+(1/4)*heterozygous+(1/2)*recessive
print('{0:.5f}'.format(1-my_prob))
