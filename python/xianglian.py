while 1:
    baoshi=list(raw_input().strip())
    maxlength=0
    i=0
    n=len(baoshi)
    for i in range(n):
        if baoshi[i]  in 'ABCDE':
            break
    newbaoshi=baoshi[i:]+baoshi[:i]
    i=0
    while i<n:
        j=i+1
        while j<n:
            if newbaoshi[j] not in 'ABCDE':
                j+=1
            else:
                break
        length=j-i-1
        if length>maxlength:
            maxlength=length
        i=j
    print maxlength
        
        
