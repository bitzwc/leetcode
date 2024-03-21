T=int(input())
Poc=[]
pa=[]
for i in range(T):
    raw1=raw_input()
    raw2=raw_input()
    n=int(raw1.strip().split(' ')[0])
    k=int(raw1.strip().split(' ')[1])
    pa.append((n,k))
    pocker=raw2.strip().split(' ')
    Poc.append(pocker)
for i in range(T):
    j=0
    pocker=Poc[i]
    n=pa[i][0]
    k=pa[i][1]
    while j<k:
        pocker1=pocker[:n]
        pocker2=pocker[n:]
        for m in range(n):
            pocker[2*m]=pocker1[m]
            pocker[2*m+1]=pocker2[m]
        j+=1
    print ' '.join(pocker)
