def f(A,r):
    n=len(A)
    while r<=n:
        B=[]
        for i in range(len(A)):
            tmp=[]
            for j in range(r):
                tmp.append(A[(i+j)%n])
            tmp.sort()
            B.append(tmp[len(tmp)/2])
        A=B
        r=r+1
    return A[0]
