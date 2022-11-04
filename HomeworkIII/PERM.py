import itertools
import math                                    
n = int(open('rosalind_perm.txt').read())                             
print(math.factorial(n))
permutation = itertools.permutations(list(range(1, n + 1)))
for el, x in enumerate(list(permutation)):                  
    results = ''                                
    for y in x:                                  
        results += str(y) + ' '              
    print(results)
    