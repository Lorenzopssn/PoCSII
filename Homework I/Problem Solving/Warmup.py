#Solve Me First
def solveMeFirst(a,b):
	# Hint: Type return a+b below
    return a+b

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)


#Simple Array Sum
import math
import os
import random
import re
import sys
def simpleArraySum(ar):
    # Write your code here
    return sum(ar)



#Compare the Triplets
import math
import os
import random
import re
import sys
def compareTriplets(a, b):
    # Write your code here
    score_a=0
    score_b=0
    x=0
    for y in a:
        if a[x]>b[x]:
            score_a += 1
        elif a[x]<b[x]:
            score_b +=1
        else:
            score_a +=0
        x += 1
    return score_a,score_b


#A Very Big Sum

import math
import os
import random
import re
import sys
def aVeryBigSum(ar):
    # Write your code here
    return sum(ar)


# Diagonal Difference
import math
import os
import random
import re
import sys
def diagonalDifference(arr):
    # Write your code here
    sum1=0
    sum2=0
    i=0
    a=len(arr)-1
    for x in arr:
        sum1 += x[i]
        i += 1
    for y in arr:
        sum2 += y[a]
        a -= 1
        
    return abs(sum1-sum2)
 

#Plus Minus
import math
import os
import random
import re
import sys
def plusMinus(arr):
    # Write your code here
    tot_pos=0
    tot_neg=0
    zeros=0
    for z in arr:
        if z==0:
            zeros += 1
        elif z<0:
            tot_neg+=1
        else:
            tot_pos+=1
    y=len(arr)
    tot_pos=tot_pos/y
    tot_neg=tot_neg/y
    zeros=zeros/y
    print("{:.6f}".format(tot_pos))
    print("{:.6f}".format(tot_neg)) 
    print("{:.6f}".format(zeros))   


#Staircase
import math
import os
import random
import re
import sys
def staircase(n):
    # Write your code here
    numberofspaces=n-1
    for element in range(1, n+1):
        print(' '*numberofspaces + '#' * element)
        numberofspaces -= 1


#Mini-Max Sum
import math
import os
import random
import re
import sys
def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min_sum=sum(arr)-arr[4]
    max_sum=sum(arr)-arr[0]
    print(min_sum, max_sum)


#Birthday Cake Candles
import math
import os
import random
import re
import sys
def birthdayCakeCandles(candles):
    # Write your code here
    candles.sort()
    return candles.count(candles[-1])

#Time Conversion
import math
import os
import random
import re
import sys
def timeConversion(s):
    # Write your code here
    if s[-2:] == 'AM':
        if s[:2]=='12':
            s='00'+s[2:8]
        else:
            s=s[:-2]
    else:
        if s[-2:]=='PM' and s[:2] != '12':
            s=str(int(s[:2])+12)+s[2:8]
        else:
            s=s[:-2]
    return s