prime=[]
n=100
a=[False]+[False]+[True]*n-1
for i in range(2,n+1):
    if a[i]==True:
        prime.append(i)
        for j in range(i*2,n+1):
            a[j] = False
print(prime)
    
