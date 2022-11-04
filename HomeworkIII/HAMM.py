startingp=open('rosalind_hamm.txt').read()
w=startingp.split('\n')
a=w[0]
b=w[1]
counter=0
for n in range(len(a)):
    if a[n] != b[n]:
        counter += 1
    else:
        pass
print(counter)
