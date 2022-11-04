#itertools.permutations()
from itertools import permutations
a=input().split()
b=str(a[0])
b=sorted(b)
c=int(a[1])
for el in permutations(b, c):
    b=''
    for i in el:
        b=b+str(i)
    print(b)


#itertools.combinations()
from itertools import combinations
a=input().split()
b=sorted(a[0])
c=int(a[1])
h=1
while h <= c:
    for el in combinations(b,h):
        t=''
        for i in el:
            t=t+str(i)
        print(t)
    h=h+1

#itertools.combinations_with_replacement()
from itertools import combinations_with_replacement
a=input().split()
b=str(a[0])
b=sorted(b)
c=int(a[1])
for el in combinations_with_replacement(b, c):
    t=''
    for i in el:
        t=t+str(i)
    print(t)


#Compress the String!
from itertools import groupby
s=list(input())
control1=[]
control2=[]
for x, y in groupby(s):
        control1.append(x)
        control2.append(list(y))
#print(control1) ['1', '2', '3', '1']
#print(control2) [['1'], ['2', '2', '2'], ['3'], ['1', '1']]
for el in control2:
    print("(", len(el), ", ", el[0], ")", end = " ", sep = "")


