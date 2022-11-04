import math
def funct(a, b):
    return math.factorial(a)/(math.factorial(b) * math.factorial(a - b))
def independent(k, n):
    x = 0
    count = 2**k                       
    for  el in range(n, count+1):
        x += funct(count, el) * 0.25**el * 0.75**(count - el)
    return x
 
if __name__ == "__main__":
    with open("/Users/lorenzopossanzini/Desktop/Rosalind/rosalind_lia.txt", "r") as f:
        k, n = [int(i) for i in f.readline().strip().split(" ")]
    print(round(independent(k,n), 3))