n=input()
arr=raw_input()
arr=arr.strip().split(' ')
arr=[int(a) for a in arr]
i=0
while i+1<len(arr):
    if arr[i]<arr[i+1]:
        i+=1
    else:
        break
j=i
while j+1<len(arr):
    if arr[j]>arr[j+1]:
        j=j+1
    else:
        break
newarr=arr[:i]+list(reversed(arr[i:j+1]))+arr[j+1:]
if newarr==sorted(arr):
    print 'yes'
else:
    print 'no'
    
