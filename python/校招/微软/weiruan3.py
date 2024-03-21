(N,M,K)=(int(x) for x in raw_input().strip().split(' '))
all_stu=[]
for i in range(N):
    line=raw_input()
    seg=line.strip().split(' ')
    number=int(seg[0])
    arrgate=int(seg[1])
    p=seg[2]
    officetime=seg[3:]
    all_stu.append((number,arrgate,officetime))
print all_stu
    
