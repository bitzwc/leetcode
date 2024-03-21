line=raw_input()
seg=line.strip().split(' ')
n=int(seg[0])
m=int(seg[1])
num=raw_input().strip().split(' ')
num=[int(x) for x in num]
k=0
for i in range(n):
    for j in range(i+1,n):
        result=num[i]^num[j]
        if result>m:
            print result
            k+=1
print k
