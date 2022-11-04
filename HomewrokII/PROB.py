import math
with open("/Users/lorenzopossanzini/Desktop/Rosalind/rosalind_prob.txt", "r") as my_input:
    s = my_input.readline().strip()
    A = map(float, my_input.readline().strip().split(" "))
y = s.count('A') + s.count('T')
x = s.count('C') + s.count('G')
for el in A:
    result = y * math.log((1-el)/2, 10) + x * math.log(el/2, 10)
    print(round(result, 3), end=" ")