st=raw_input()
l=st.strip().split(' ')
n=int(l[0])
s=int(l[1])
L=int(l[2])
while n>100 or s>L or L>10000:
    st=raw_input()
    l=st.strip().split(' ')
    n=int(l[0])
    s=int(l[1])
    L=int(l[2])
m=(L+1)/(s+1)
if m%13==0:
    m=m-1
if n%m==0:
    print n/m
elif (n%m)%13!=0:
    print n/m+1
else:
    print n/m+2

