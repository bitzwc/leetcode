l,r,m=raw_input().split()
l=int(l)
r=int(r)
m=int(m)
n=0
for i in range(l,r+1):
    i=bin(i)
    if m==i.count('1'):
        n+=1
if n>0:
    print n
else:
    print -1
