import numpy as np

n = int(input())

arr = np.random.randint(0, 10, (n,n)) 
print(arr)

maxinmin = -1

for i in range(3):
    small = min(arr[i])
    if(maxinmin<small) : maxinmin = small

print(maxinmin)
    
