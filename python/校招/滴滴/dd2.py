import sys
d={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
for line in sys.stdin:
    a=line.split()
    for x in a:
        l=list(x[2:])
        l.reverse()
        y=0
        for i in range(len(l)):
            if l[i] in d.keys():
                y=y+d[l[i]]*pow(16,i)
            else:
            	y=y+int(l[i])*pow(16,i)
        print y
