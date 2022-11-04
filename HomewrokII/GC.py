start=open('rosalind_gc.txt')
strands=start.readlines()
temp=''
data=[]
counter=1
while counter<len(strands):
    if '>' in strands[counter]:
        data.append(temp)
        data.append(strands[counter])
        temp= ''
        counter +=1        
    else:
        temp+= strands[counter]
        counter += 1
data.append(temp)
data.insert(0, strands[0])
for n in range(len(data)):
    data[n] = data[n].replace('\n','')
    data[n] = data[n].replace('>','')

name_of_the_string=''
gc_content=0
for q in range(1, len(data), 2):
    gc=data[q].count('G')+data[q].count('C')
    gcpercent=(gc/len(data[q]))*100
    if gcpercent>gc_content:
        gc_content=gcpercent
        name_of_the_string=''
        name_of_the_string=name_of_the_string+data[q-1]
print(name_of_the_string)
print(round(gc_content, 6))