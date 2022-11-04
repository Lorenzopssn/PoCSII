with open('rosalind_tree.txt', 'r') as f:
    inp = []             
    for el in f:                              
        inp.append([int(x) for x in el.split()])                    
n = inp[0][0]                                     
edg = inp[1:]                                   
print(n - len(edg) - 1) 