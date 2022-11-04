# DefaultDict Tutorial
from collections import defaultdict
a=defaultdict(list)
b=[]
q=input().split(' ')
n=int(q[0])
m=int(q[1])
for _ in range(0,n):
    #i append each object with its relative position each time it is repeated
    a[input()].append(_+1) 
for x in range(0,m):
    b=b+[input()]  
for j in b: 
    if j in a:
        outcome=' '
        outcome=outcome.join(map(str, a[j]))
        print(outcome)
    else:
        print (-1)


#Collections.namedtuple()
from collections import namedtuple
n=int(input())
name_characteristics=input().split()

marks_sum=0
student_model=namedtuple('student', name_characteristics)
for el in range(n):
    characteristics=input().split()
    single_student=student_model(characteristics[0],characteristics[1],characteristics[2],characteristics[3])
    marks_sum += int(single_student.MARKS)
print('{:.2f}'.format(marks_sum/n))


#Word Order
from collections import Counter

a = Counter(input() for x in range(int(input())))
print(len(a))
print(*a.values())


#Collections.OrderedDict()
from collections import*
my_input = int(input())
my_OD = OrderedDict()
for x in range(my_input):
    item = input().split()
    price = int(item[-1])
    name = " ".join(item[:-1])
    if(my_OD.get(name)):
        my_OD[name] += price
    else:
        my_OD[name] = price
for x in my_OD.keys():
    print(x, my_OD[x])
