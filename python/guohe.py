N=input()
line=raw_input()
arr=line.strip().split(' ')
arr=[int(x) for x in arr]
i=0
k=0
while i<N:
    if arr[i]!=0:
        i+=arr[i]
        k+=1
    else:
        k=-1
        break
print k
