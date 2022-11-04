#Find Angle MBC
import math
ab=int(input())
bc=int(input())
x=ab/bc
t=round(math.degrees(math.atan(x)))
degree=chr(176)
print(str(t)+degree)


#Mod Divmod
a=int(input())
b=int(input())
print(a//b)
print(a%b)
print(divmod(a, b))


#Power - Mod Power
a=int(input())
b=int(input())
m=int(input())
print(pow(a,b))
if b > 0:
    print(pow(a,b,m))


#Triangle Quest
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i)//9)*i)