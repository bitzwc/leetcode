def merge_sort(A,p,r):
    if p<r:
        q=int((p+r)/2)
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
    return A
def merge(A,p,q,r):
    L=A[p:q+1]
    R=A[q+1:r+1]
    i=0
    j=0
    for k in range(p,r+1):
        if i<len(L) and j<len(R):
            if L[i]<R[j]:
                A[k]=L[i]
                i+=1
            else:
                A[k]=R[j]
                j+=1
        elif j<len(R):
            A[k]=R[j]
            j+=1
        elif i<len(L):
            A[k]=L[i]
            i+=1
print(merge_sort([3,1,2,4],0,3))
