x=open('rosalind_fib.txt').read().split(' ')
n=int(x[0])
k=int(x[1])
parents=1
offspring=k
for i in range(n-2):
    temp=parents
    parents=parents+offspring
    offspring=temp*k
print(parents)
