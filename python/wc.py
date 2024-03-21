m=raw_input()
while int(m)<0 or int(m)>10000:
    m=raw_input()
N=int(m)
def wc(N,s):
    if N%1111==0:
        print "%s - %s = 0000" %(s,s)
    elif N!=6174:
        a=N%10
        b=(N/10)%10
        c=(N/100)%10
        d=(N/1000)%10
        l1=sorted([str(a),str(b),str(c),str(d)])
        y=int(''.join(l1))
        l1.reverse()
        z=int(''.join(l1))
        print ("%4d" %z).replace(' ','0')+' - '+("%4d" %y).replace(' ','0')+' = ' +("%4d" %(z-y)).replace(' ','0')
        wc(z-y,('%4d' %(z-y)).replace(' ','0'))
    
wc(N,m)
