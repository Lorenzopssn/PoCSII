 #CamelCase
import math
import os
import random
import re
import sys
def camelcase(s):
    # Write your code here
    counter=1
    for x in s:
        if x.isupper():
            counter += 1
    return counter


#Strong Password
import math
import os
import random
import re
import sys
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    my_special_char='!@#$%^&*()-+'
    final=0
    upper_counter=0
    lower_counter=0
    spch_counter=0
    digit_counter=0
    for x in password:
        if x.isupper():
            upper_counter += 1
        if x.islower():
            lower_counter += 1
        if x.isdigit():
            digit_counter += 1
        if x in my_special_char:
            spch_counter +=1
    if upper_counter == 0:
        final += 1
    if lower_counter == 0:
        final += 1
    if digit_counter == 0:
        final += 1
    if spch_counter == 0:
        final += 1
    if final==0 and n>6:
        return 0
    if final != 0:
        if n + final > 6:
            return final
        else:
            final += ((6-n)-final)
            return final
    else:
        return 6-n


#Mars Exploration
import math
import os
import random
import re
import sys
def marsExploration(s):
    # Write your code here
    changed_letters=0
    n = 3
    a=[]
    x=0
    b=int(len(s)/3)
    for i in range(0, b):
        a.append(s[x:x+n])
        x += n
    for element in a:
        if element[0]!= 'S':
            changed_letters += 1
        if element[1] != 'O':
            changed_letters += 1
        if element[2] != 'S':
            changed_letters += 1
    return changed_letters


#Pangrams
import math
import os
import random
import re
import sys
def pangrams(s):
    # Write your code here
    my_alphabet='abcdefghijklmnopqrstuvwxyz'
    for n in my_alphabet:
        if n not in s.lower():
            return 'not pangram'

    return 'pangram'


#Making Anagrams
import math
import os
import random
import re
import sys
def makingAnagrams(s1, s2):
    # Write your code here
    shorter=''
    longer=''
    counter=0
    if len(s1)>len(s2):
        shorter=shorter+s2
        longer=longer+s1
    else:
        shorter=shorter+s1
        longer=longer+s2
    for el in longer:
        counter += abs(longer.count(el)-shorter.count(el))
        longer=longer.replace(el, '')
        shorter=shorter.replace(el, '')
    if len(longer) != 0:
        for x in longer:
            counter += longer.count(x)
            longer=longer.replace(x, '')
    if len(shorter) != 0:
        for y in shorter:
            counter += shorter.count(y)
            shorter=shorter.replace(y, '')
    return counter