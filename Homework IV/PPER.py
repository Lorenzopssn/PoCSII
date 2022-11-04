a = 100
b = 10
count = 1
for x in range(b):
    count = count * (a - x)
print(count % 1000000)