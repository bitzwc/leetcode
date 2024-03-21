def maxHeap(A,i,heap_size):
    l = 2*i
    r = 2*i+1
    if l<heap_size and A[l]>A[i]:
        largest = l
    else:
        largest = i
    if r<heap_size and A[r]>A[largest]:
        largest = r
    if largest != i:
        temp = A[i]
        A[i]=A[largest]
        A[largest]=temp
        maxHeap(A,largest,heap_size)
def buildMaxHeap(A):
    heap_size = len(A)
    for i in range(int(heap_size/2),-1,-1):
        maxHeap(A,i,heap_size)
def heapSort(A):
    buildMaxHeap(A)
    n=len(A)
    heap_size=n
    for i in range(n-1,0,-1):
        temp=A[i]
        A[i]=A[0]
        A[0]=temp
        heap_size=heap_size-1
        maxHeap(A,0,heap_size)
    return A
print(heapSort([4,1,3,2,16,9,10,14,8,7]))
