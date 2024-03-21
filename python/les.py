import sys
for line in sys.stdin:
    l=line.strip().split(' ')
    m=l[0]
    n=l[1]
    result=[]
    for x in range(int(m),int(n)):
        s=0
        for num in list(str(x)):
            s=s+pow(int(num),3)
        if s==x:
            result.append(str(x))
    if len(result)==0:
        print "no"
    else:
        print ' '.join(result)
     
