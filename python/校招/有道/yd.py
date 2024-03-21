while 1:
    enemy=raw_input().strip().split(' ')
    loca=raw_input().strip().split(' ')
    n=int(enemy[0])
    a=int(enemy[1])
    b=int(enemy[2])
    loca=[int(x) for x in loca]
    k=0
    out=[]
    while max(loca)>=0:
        i=loca.index(max(loca))
        for j in range(n-1,i,-1):
            if loca[j]==max(loca):
                i=j
        loca[i]=loca[i]-a
        if i-1 in range(n):
            loca[i-1]=loca[i-1]-b
        if i+1 in range(n):
            loca[i+1]=loca[i+1]-b
        out.append(str(i+1))
    print len(out)
    print ' '.join(out)
