in1=raw_input()
m=int(in1.strip().split(' ')[1])
in2=raw_input()
result=[]
check=in2.strip().split(' ')
for i in range(m):
    in3=raw_input()
    seg3=in3.strip().split(' ')
    p=int(seg3[0])
    x=int(seg3[1])
    y=int(seg3[2])
    if p==1:
        result.append(min(check[x-1:y]))
    elif p==2:
        check[x-1]=str(y)
print ' '.join(result)+' '
