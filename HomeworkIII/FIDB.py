
with open("rosalind_fibd.txt", "r") as my_input:
    n, m = map(int, my_input.readline().strip().split(" "))                                                                                                                                      
bunnies=[1, 1]                                                           
y = 2  
x = 0                                                                   
while y < n:                                                              
    if y < m:                                                             
        bunnies.append(bunnies[-2] + bunnies[-1])                              
    elif y == m or x == m + 1:                                        
        bunnies.append(bunnies[-2] + bunnies[-1] - 1)                          
    else:                                                                      
        bunnies.append(bunnies[-2] + bunnies[-1] - bunnies[-(m + 1)])                                                           
    y += 1                                                                
print(bunnies[-1])   
  
