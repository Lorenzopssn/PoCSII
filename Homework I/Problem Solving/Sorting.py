#Intro to Tutorial Challenges
import math
import os
import random
import re
import sys
def introTutorial(V, arr):
    # Write your code here
    return arr.index(V)


#Insertion Sort - Part 1
import math
import os
import random
import re
import sys
def insertionSort1(n, arr):
    # Write your code here
    mv=arr[n-1]
    m=n-2
    h=n-1
    while mv<arr[m]:
        if m >= 0:
            outcome=''
            arr[h]=arr[m]
            m -= 1
            h -= 1
            for el in arr:
                outcome=outcome+str(el)+' '
            print(outcome[:-1])
        else:
            my_final=''
            arr[h]=mv
            for el in arr:
                my_final=my_final+str(el)+' '
            print(my_final[:-1]) 
            break
            

    else:
        k=''
        arr[h]=mv
        for el in arr:
            k=k+str(el)+' '
        print(k[:-1])


#Insertion Sort - Part 2
import math
import os
import random
import re
import sys
def insertionSort1(start, arr):
    a= arr[start]
    for el in range(start-1, -1, -1):
        if arr[el] > a:
            arr[el+1] = arr[el]
        else:
            arr[el+1] = a
            break
    if arr[0] > a:
        arr[0] = a

def insertionSort2(n, arr):
    # Write your code here
    for el in range(1, len(arr)):
        insertionSort1(el, arr)
        print(" ".join(map(str, arr)))


#Correctness and the Loop Invariant
def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1 
        key = l[i]
        while (l[j] > key) and (j >= 0):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
m = input()
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))


#Running Time of Algorithms
import math
import os
import random
import re
import sys
def insertionSort1(i, a):
    inp = a[i]
    out = 0
    
    for x in range(i-1, -1, -1):
        if a[x] > inp:
            out += 1
            a[x+1] = a[x]
        else:
            a[x+1] = inp
            break
    if a[0] > inp:
        a[0] = inp
        
    return out

def insertionSort2(n, second):
    result = 0
    for y in range(1, len(second)):
        result += insertionSort1(y, second)
    return result

def runningTime(arr):
    # Write your code here
    return insertionSort2(len(arr), arr)


#Quicksort 1 - Partition
import math
import os
import random
import re
import sys
def quickSort(arr):
    # Write your code here
    left = []
    equal = []
    right = []
    pivot = arr[0]
    
    for el in arr:
        if el < pivot:
            left.append(el)
        elif el == pivot:
            equal.append(el)
        elif el > pivot:
            right.append(el)


#Counting Sort 2
import math
import os
import random
import re
import sys
def countingSort(arr):
    # Write your code here
    count = [0] * (max(arr) + 1)
    out = [0] * (len(arr))
    total = 0
    for el in arr:
        count[el] += 1
    for i in range(len(count)):
        old = count[i]
        count[i] = total
        total += old
    for x in arr:
        out[count[x]] = x
        count[x] += 1
        
    return out


#The Full Counting Sort
import math
import os
import random
import re
import sys
def countSort(arr):
    # Write your code here
    res= [[] for el in range(100)]
    for el in range(n//2):
        res[int(arr[el][0])].append('-')
    for x in range(n//2, n):
        res[int(arr[x][0])].append(arr[x][1])
    for y in res:
        if y:
            print(*y, end=' ')

#Closest Numbers
import math
import os
import random
import re
import sys
def closestNumbers(arr):
    out = []
    arr = sorted(arr)
    a = 10**7
    
    for x in range(1, len(arr)):
        dif = abs(arr[x-1] - arr[x])
        
        if dif < a:
            out = [(arr[x-1], arr[x])]
            a = dif
        elif dif == a:
            out.append((arr[x-1], arr[x]))
             
    result = [item for el in out for item in el]
       
    return result


#Find the Median
import math
import os
import random
import re
import sys
def findMedian(arr):
    # Write your code here
    arr = sorted(arr)
    out = arr[len(arr)//2]
    return out
