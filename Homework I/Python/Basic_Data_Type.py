# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    b= list(arr)
    our_maximum=int(max(b))
    while max(b)==our_maximum:
        b.remove(max(b))
    if max(b)!=our_maximum:
        print(max(b))

# Nested Lists
if __name__ == '__main__':
    my_list=[]
    final_students=[]
    for _ in range(int(input())):
        temp=[]
        name = input()
        score = float(input())
        temp.append(name)
        temp.append(score)
        my_list.append(temp)
    clock=[1000]
    final_students=[]
    for lists in my_list:
        b=lists[1]
        if b <= clock[0]:
            clock.pop()
            clock.append(b)
    for el in my_list:
        b=el[1]
        if b == clock[0]:
            my_list.remove(el)
    for el in my_list:
        b=el[1]
        if b == clock[0]:
            my_list.remove(el)
    second_lowest=[10000]
    for lists in my_list:
        b=lists[1]
        if b < second_lowest[0]:
            second_lowest.pop()
            second_lowest.append(b)
    for lists in my_list:
        b=lists[1]
        if b == second_lowest[0]:
            final_students.append(lists[0])
    final_students=sorted(final_students)
    for el in final_students:
        print(el)

#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

x=sum(student_marks[query_name])/3
y="{:.2f}".format(x)
print(y)

#Lists
if __name__ == '__main__':
    N = int(input())
    idk=[]
    final_list=[]
    for i in range(N):
        idk.append(input())
    for el in idk:
        k=el.split(' ')
        if 'print' in k:
            print(final_list)
        if 'pop' in k and len(final_list) != 0:
            final_list.pop()
        if 'reverse' in k:
            final_list.reverse()
        if 'sort' in k:
            final_list.sort()
        if 'insert' in k:
            a=[]
            for i in k:
                a.append(i)
            final_list.insert(int(a[1]), int(a[2]))
        if 'remove' in k:
            b=[]
            for i in k:
                b.append(i)
            final_list.remove(int(b[1]))
        if 'append' in k:
            c=[]
            for i in k:
                c.append(i)
            final_list.append(int(c[1]))

#Tuples
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print(hash(tuple(integer_list)))
