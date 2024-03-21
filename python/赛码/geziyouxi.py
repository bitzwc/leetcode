line=raw_input()
seg=line.strip().split(' ')
n=int(seg[0])
m=int(seg[1])
quan_list=[]
for i in range(n):
    quan=input()
    quan_list.append(quan)
for j in range(m):
    line=raw_input()
    seg=line.strip().split(' ')
    typ=int(seg[0])
    a=int(seg[1])
    b=int(seg[2])
    if typ==1:
        quan_list[a-1]=b
    elif typ==2:
        print sum(quan_list[a-1:b])
    elif typ==3:
        print max(quan_list[a-1:b])
        
