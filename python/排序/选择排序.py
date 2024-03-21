def selectSort(arr):
    for j in range(len(arr)-1):
        key=arr[j]
        for i in range(j,len(arr)):
            if key>=arr[i]:
                key=arr[i]
                k=i
        arr[k]=arr[j]
        arr[j]=key
    return arr
print(selectSort([3,2,4,1,5,8]))
print(selectSort([1,2,3]))
