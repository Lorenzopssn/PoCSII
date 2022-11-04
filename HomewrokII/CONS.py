strands=open('rosalind_cons.txt').readlines()
temp=''
data=[]
counter=1
while counter<len(strands):
    if '>' in strands[counter]:
        data.append(temp)
        data.append(strands[counter])
        temp= ''
        counter +=1        
    else:
        temp+= strands[counter]
        counter += 1
data.append(temp)
for n in range(len(data)):
    data[n] = data[n].replace('\n','')
for el in data:
    if 'Rosalind' in el:
        data.remove(el)
A=[]
C=[]
G=[]
T=[]
out=''
for i in range(len(data[0])):
    counterA=0
    counterC=0
    counterG=0
    counterT=0    
    for el in data:
        if el[i] == 'A':
            counterA +=1
        elif el[i] == 'C':
            counterC +=1
        elif el[i] == 'G':
            counterG +=1
        else:
            counterT +=1 
    A.append(counterA)
    C.append(counterC)
    G.append(counterG)
    T.append(counterT)

for i in range(len(A)):
    t=max(A[i],C[i],G[i],T[i])
    if t == A[i]:
        out+='A'
    elif t == C[i]:
        out+='C'
    elif t== G[i]:
        out+='G'
    else:
        out+='T'
print(out)
print('A:',*A)
print('C:',*C)
print('G:',*G)
print('T:',*T)