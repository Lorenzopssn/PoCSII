# Symmetric difference
M=input().split()
len_N=(int(input()))
N=input().split()
a=set(list(map(int, M)))
b=set(list(map(int, N)))
c=[]
for el in a.difference(b):
        c.append(el)       
for el in b.difference(a):
        c.append(el)
c=sorted(c)
for el in c:
    print(el


#Set .add()
n=int(input())
a=[]
for i in range(n):
    a.append(input())
my_set=set()
for i in a:
    if i not in my_set:
        my_set.add(i)
print(len(my_set))


#Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
m=int(input())
a=[]
for i in range(m):
    a.append(input())
for el in a:
    if 'pop' in el:
        s.pop()
    else:
        b=int(el[-1])
        if 'discard' in el:
            s.discard(b)
        if 'remove' in el:
            s.remove(b)
print(sum(s))


#Set .union() Operation
a=input()
b=set()
c=input().split(' ')
for el in c:
    b.add(el)

d=input()
e=set()
f=input().split(' ')
for el in f:
    e.add(el)

g=b.union(e)
print(len(g))
