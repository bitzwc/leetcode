T=input()
for i in range(T):
    number=raw_input()
    number=number.strip()
    cishu=[0]*10
    cishu[0]=number.count('Z')
    cishu[2]=number.count('W')
    cishu[4]=number.count('U')
    cishu[1]=number.count('O')-cishu[0]-cishu[2]-cishu[4]
    cishu[3]=number.count('R')-cishu[0]-cishu[4]
    cishu[5]=number.count('F')-cishu[4]
    cishu[6]=number.count('X')
    cishu[7]=number.count('V')-cishu[5]
    cishu[8]=number.count('G')
    cishu[9]=(number.count('N')-cishu[1]-cishu[7])/2
    num=''
    for j in range(10):
        num+=cishu[j]*str(j)
    num=list(num)
    num=[str((int(x)-8)%10) for x in num]
    num.sort()
    print ''.join(num)
