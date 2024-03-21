N,M,t1,t2=raw_input().strip().split(' ')
N=int(N)
M=int(M)
t1=int(t1)
t2=int(t2)
V=list(range(1,N+1))
E=[]
for i in range(M):
    (a,b)=raw_input().strip().split(' ')
    a=int(a)
    b=int(b)
    E.append((a,b))
print V,E
