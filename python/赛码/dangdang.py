n=input()
i=2
j=1
while j<n:
    i+=1
    for k in range(2,i):
        if i%k==0:
            break
        elif k==i-1:
            j+=1
print i
            
