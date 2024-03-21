def quickSort(A,p,q):
    if p>=q:
        return A
    key=A[p]
    i=p
    j=q
    while i<j:
        while i<j and A[j]>=key:
            j-=1
        A[i]=A[j]
        while i<j and A[i]<=key:
            i+=1
        A[j]=A[i]
    A[i]=key
    quickSort(A,p,i-1)
    quickSort(A,i+1,q)
    return A
print(quickSort([3,2,1,4,0],0,4))