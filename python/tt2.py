n=input()
nan=raw_input()
nan=nan.strip().split(' ')
nan=[int(x) for x in nan]
nan.sort()
n=len(nan)
i=0
need=0
while i<n:
    j=i+1
    k=1
    while j<n:
        if nan[j]-nan[i]<=20:
            i=j
            j+=1
            k+=1
            if k>3:
                k=k-3
    i=j
    need +=3-k
print need
