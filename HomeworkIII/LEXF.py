import itertools
 
with open("rosalind_lexf.txt") as my_input:
    data = my_input.read().split()
    x = data[:-1]
    n = int(data[-1])
perm = itertools.product(x, repeat = n)
final = []
for i, j in enumerate(list(perm)):
    permutation = ''
    for el in j:
        permutation += str(el)
    final.append(permutation)
final.sort()
for el in final:
    print(el, end="\n")