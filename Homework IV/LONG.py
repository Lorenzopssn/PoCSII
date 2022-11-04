from Bio import SeqIO
f = open('rosalind_long.txt', 'r')
my_sequences = []
store = []
for el in SeqIO.parse(f, 'fasta'):
    my_sequences.append(str(el.seq))
for a, b in enumerate(my_sequences):
  count = (len(b)+1)//2
  for c, d in enumerate(my_sequences):
    if a != c:
      var = d.find(b[-count:])
      if var >= 0 and b[-count-var:]==d[:count+var]:
        store.append((a,c,count+var))
l = [el[0] for el in store]
r = [el[1] for el in store]
start = set(l) - set(r) 
out = ""
fragment= list(start)[0]
while True:
    out += my_sequences[fragment]
    x = [x for x in store if x[0]==fragment]
    if x:
        fragment = x[0][1]
        out = out[:-x[0][2]]
    else:
        break
print(out)